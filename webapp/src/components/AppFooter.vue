<template>
  <footer>
    <h4>About us</h4>
    <p>Phones: +375297274086<br>
      <span>+375291282788</span><br>
      <span>+375296457847</span>
    </p>
    <div>Copyright &copy; {{ year }}</div>
  </footer>
</template>

<script>
import { computed } from '@vue/reactivity'

export default {
  name: 'AppFooter',
  setup () {
    const year = computed(() => new Date().getFullYear())
    return { year }
  }
}
</script>

<style lang="scss">
  footer {
    position: initial; /* Фиксированное положение */
    left: 0; bottom: 0; /* Левый нижний угол */
    padding: 1px; /* Поля вокруг текста */
    background: #00BBD6; /* Цвет фона */
    color: midnightblue; /* Цвет текста */
    width: 100%;
    min-height: 90px;
}
  footer h4 {
    text-align: center;
    margin: 2px;
  }
  footer div {
    font-size: 70%;
  }
  footer p {
    font-size: 75%;
    text-align: -webkit-right;
    margin: 20px;
  }
</style>
