<template>
  <div class="v-popup">
      <div class="v-popup_header">
        <main class="form-signup">
          <form>
            <span>
              <i class="material-icons" @click="closeRegister">close</i>
            </span><br><br>
            <h1 class="h3 mb-3 fw-normal">Please sign up</h1>
              <input v-model="user.username" type="text" class="form-control" placeholder="Username" required>
              <input v-model="user.email" type="email" class="form-control" placeholder="Email" required>
              <input v-model="user.password" type="password" class="form-control" placeholder="Password" required>
            <input class="w-100 btn btn-lg btn-primary" type="button" value="signIn" @click="signIn"/>
          </form>
        </main>
      </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios'

export default {
  name: 'Register',
  data () {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      }
    }
  },
  // setup () {
  //   const data = reactive({
  //     username: '',
  //     email: '',
  //     password: ''
  //   })
  //   const submit = async () => {
  //     await fetch('http://localhost:8000/home-work/register/', {
  //       method: 'POST',
  //       headers: { 'Content-Type': 'application/json' },
  //       credentials: 'include',
  //       body: JSON.stringify(data)
  //     })
  //   }
  //   return {
  //     data,
  //     submit
  //   }
  // },
  methods: {
    closeRegister () {
      this.$emit('closeRegister')
    },
    signIn () {
      axios.post('http://localhost:8000/home-work/register/', {
        username: this.user.username,
        email: this.user.email,
        password: this.user.password
      }).then(response => { this.user = response.data; alert('Welcome:)'); this.closeRegister() })
    }
  }
}
</script>
  // methods: {
  //   async signUp () {
  //     const res = await fetch('http://localhost:800/home-work/register', {
  //       method: 'POST',
  //       headers: {
  //         'Content Type': 'application/json'
  //       },
  //       credentials: 'include',
  //       body: JSON.stringify({
  //         email: this.form.email,
  //         password: this.form.password,
  //         username: this.form.username
  //       })
  //     })
  //     console.log(res)
  // },
