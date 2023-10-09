<template>
  <div class="login">
    <div>
      <form @submit.prevent="submit">
        <div>
          <label for="username">Username:</label>
          <input v-model="form.username" name="username" type="text"/>
        </div>
        <div>
          <label for="password">Password:</label>
          <input v-model="form.password" name="password" type="password"/>
        </div>
        <button type="submit">Submit</button>
      </form>


      <div v-if="showError" id="error">
        <div class="error"> User not found</div>
        <div onclick="this">
          Not registered?
          <button>Register</button>
        </div>
      </div>

    </div>
  </div>
</template>

<script>


import {mapActions} from "vuex";
import axios from "axios";

export default {
  name: "LoginView",
  components: {},
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["Register"]),
    async submit() {
      const formData = {
        'username': this.form.username,
        'password': this.form.password,
      }
      console.log(formData)
      await axios.post(`api/v1/token/login/`, formData)
          .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = `Token ${token}`
            localStorage.setItem('token', token)


            this.$router.push('/properties')
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
};
</script>

<style scoped>
.error {
  color: red !important;
  padding-top: 20px;
  padding-bottom: 20px;
}
</style>