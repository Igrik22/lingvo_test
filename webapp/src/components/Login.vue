<template>
  <div class="v-popup">
      <div class="v-popup_header">
        <main class="form-signin">
          <form>
            <span>
              <i class="material-icons" @click="closeLogin">close</i>
            </span><br><br>
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
              <input v-model="user.email" type="email" class="form-control" placeholder="Email" required>
              <input v-model="user.password" type="password" class="form-control" placeholder="Password" required>
            <input class="w-100 btn btn-lg btn-primary" type="button" value="sign in" @click="signIn"/>
          </form>
        </main>
      </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      user: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    closeLogin () {
      this.$emit('closeLogin')
    },
    signIn () {
      axios.post('http://localhost:8000/home-work/login/', {
        email: this.user.email,
        password: this.user.password
      }).then(response => {
        this.user = response.data
        alert('Спасибо что Вы с нами:)')
        this.closeRegister()
      })
    }
  }
}
</script>
