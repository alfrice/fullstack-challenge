<template>
  <img alt="Vue logo" src="./assets/wdlogo.jpg">
  <CodeChallengeHome msg="Welcome to Your Vue.js App"/>
</template>

<script>
import CodeChallengeHome from './components/CodeChallengeHome.vue'
import axios from "axios";

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token;
    axios.defaults.headers.common[`Token ${token}`]

  },
  components: {
    CodeChallengeHome
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
  margin-bottom: 60px;
}

input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}
</style>
