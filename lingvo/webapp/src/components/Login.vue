<template>
    <div class="v-popup">
      <div class="v-popup_header">
        <span>
            <i class="material-icons" @click="closeLogin">close</i>
        </span><br><br>
        <span>Enter login and password</span><br><br>
      </div>
      <div class="v-popup_content">
          <slot></slot>
      </div>
      <div class="v-popup_footer">
        <button class="submit_btn" @click="setLogin">enter</button>
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
      login: '',
      password: ''
    }
  },
  methods: {
    setLogin () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/jwt/refresh/',
        type: 'POST',
        data: {
          username: this.login,
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

<style lang="scss">
  .v-popup {
    margin-left: -240px;
    padding: 30px;
    position: absolute;
    align-items: center;
    top: 100px;
    background: gray;
    &__header, &__foter {
      display: initial;
      justify-content: center;
      align-items: center;
      position: absolute;
      width: 200px;
    }
    input {
      display: compact;
      justify-content: center;
      align-items: center;
      background: yellow;
      border-radius: 14px;
      width: 150px;
      height: 3px;
    }
    .submit_btn {
      padding: 8px;
      color: white;
      background: black;
    }
    i {
      color: red;
      }
}
</style>
