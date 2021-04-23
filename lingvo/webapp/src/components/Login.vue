<template>
  <div class="v-popup">
      <div class="v-popup_header">
        <main class="form-signin">
          <form>
            <span>
              <i class="material-icons" @click="closeLogin">close</i>
            </span><br><br>
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
              <input type="email" class="form-control" placeholder="Email" required>
              <input type="password" class="form-control" placeholder="Password" required>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
          </form>
        </main>
      </div>
    </div>
</template>

<script>
import { $, jQuery } from 'jquery'

window.jQuery = jQuery

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    setLogin () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/jwt/refresh/',
        type: 'POST',
        data: {
          username: this.email,
          password: this.password
        },
        success: (response) => {
          alert('Спасибо что Вы с нами')
          sessionStorage.setItem('auth_token', response.data.attributes.auth_token)
          this.$router.push({ name: 'Home' })
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Логин или пароль не верен')
          }
        }
      })
    },
    closeLogin () {
      this.$emit('closeLogin')
    }
  }
}
</script>
