<script setup>
import {defineEmits, defineProps, ref} from 'vue';
import axios from "axios";

defineProps(['data', 'expanded'])
const emits = defineEmits(['update:expanded', 'itemDeleted'])
const expanded = ref(false)
const deleteRow = function (id) {
  axios.delete(`api/v1/listings?id=${id}`)
      .then(() => {
        emits("itemDeleted");
      })
      .catch(error => {
        console.error(error)
      })
}
</script>

<template>
  <hr/>
  <div class="listing">
    <div class="listing" @click="expanded=!expanded">
      <div>{{ data.Address }} {{ data.Zip }}</div>
      <div>{{ data.CLASS_DESCRIPTION }}</div>
      <div>${{ data.ESTIMATED_MARKET_VALUE }}</div>
    </div>

    <div>
      <button @click="deleteRow(data.id)">Delete</button>
    </div>
  </div>
  <div v-if="expanded">
    <div v-for="(k) in Object.keys(data)" v-bind:key="k" class="flex-container">
      <div><b>{{ k }}</b></div>
      <div>{{ data[k] }}</div>
    </div>
  </div>
</template>

<style>
div {
  margin-left: 20px;
  padding: 0;
}

.listing {
  display: flex;
  flex-direction: column;
}

.flex-container {
  flex-direction: row;
  margin-left: 30px;

  display: flex;
}

.flex-container > div {
  font-size: 8px;
  padding: 0;
}
</style>