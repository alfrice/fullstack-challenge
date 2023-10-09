<template>
  <div class="hello">
    <router-link v-if="!isLoggedIn" to="/login"><span>Login</span></router-link>
    <router-link v-if="!isLoggedIn" to="/register"><span>Register</span></router-link>
    <router-link v-if="isLoggedIn" to="/properties"><span> Properties</span></router-link>
    <router-link v-if="isLoggedIn" to="/logout">Logout</router-link>
  </div>

  <router-view></router-view>
</template>

<script>
export default {
  name: 'CodeChallengeHome',
  props: {
    msg: String
  },
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated
    }
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

span {
  padding-left: 10px;
  padding-right: 10px;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #294e84;
}
</style>
