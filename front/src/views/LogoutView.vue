<template>
  <div>logout</div>
</template>

<script>

import axios from "axios";

export default {
  name: "LogoutView",
  components: {},
  mounted() {
    this.$store.commit('removeToken')
    axios.defaults.headers.common['Authorization'] = `Token `
    localStorage.setItem('token', '')
    this.$router.push('/login')
  }

};
</script>

<style scoped>
.error {
  color: red !important;
  padding-top: 20px;
  padding-bottom: 20px;
}
</style>