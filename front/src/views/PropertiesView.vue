<script>
// @ is an alias to /src

import RealEstateListingComponent from "@/components/RealEstateListingComponent.vue";
import axios from "axios";


export default {
  name: "PropertiesView",
  components: {RealEstateListingComponent},
  data() {
    return {search: "", listings: []}
  },

  mounted() {
    const axiosConfig = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',

    }
    axios.get(`api/v1/listings`, axiosConfig)
        .then(response => {
          this.listings = response['data'];
        })
        .catch(error => {
          console.error(error)
        })


  },
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated
    }
  },
  methods: {


    refreshPage() {
      const axiosConfig = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',

      }
      axios.get(`api/v1/listings`, axiosConfig)
          .then(response => {
            this.listings = response['data'];
          })
          .catch(error => {
            console.error(error)
          })
    },

    filterList() {
      return this.listings?.filter((listing) => {
        var keys = ['Address', 'Zip', 'ESTIMATED_MARKET_VALUE', 'BLDG_USE', 'BUILDING_SQ_FT']
        for (const i in keys) {
          const value = listing[keys[i]]
          if (value && value.toLowerCase().includes(this.search) || value.includes(this.search)) {
            return true;
          }

        }

        return false;

      });
    }
  }
};
</script>

<template>
  <div v-if="isLoggedIn" class="home">
    <input v-model="search" placeholder="Search" type="text"/>

    <div v-if="search&&!filterList(search).length" class="item error">
      <p>No results found!</p>
    </div>
    <div v-for="(item, index) in filterList(search)" v-bind:key="index">
      <real-estate-listing-component :key="index" v-bind:data="item" @itemDeleted="refreshPage"/>
    </div>

  </div>
</template>

