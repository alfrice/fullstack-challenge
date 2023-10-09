<template>
  <div class="signup">
    <form @submit.prevent="submit">
      <div>
        <label for="username">Username:</label>
        <input v-model="form.username" name="username" type="text"/>
      </div>
      <div>
        <label for="email">e-mail:</label>
        <input v-model="form.email" name="email" type="text"/>
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="form.password" name="password" type="password"/>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
  <p v-if="showError" id="error">Username already exists</p>
</template>

<script>
import {mapActions} from "vuex";
import axios from 'axios';

export default {
  name: "RegisterView",
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
        'email': this.form.email,
      }
      console.log(formData)
      await axios.post(`api/v1/users/`, formData)
          .then(response => {

            this.$router.push('/login')
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      try {
        await this.Register(this.form);
        this.$router.push("/properties");
        this.showError = false
      } catch (error) {
        this.showError = true
      }
    },
  },
};
</script>
<style scoped>

#error {
  color: red;
}

.signup {
  padding: 20px;
  display: block;
  width: 50%
}
</style>