<template>
  <app-header />
  <router-view/>
  <AppSlider
    :slider_data="sliderItems"
    :interval="1000"
  />
  <app-footer />
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'
import AppSlider from '@/components/AppSlider'

export default {
  name: 'app',
  data () {
    return {
      sliderItems: [
        { id: 1, name: '1', img: '1.jpg' },
        { id: 2, name: 'bridge', img: '2.jpg' },
        { id: 3, name: '3', img: '3.jpg' },
        { id: 4, name: '4', img: '4.jpg' },
        { id: 5, name: '5', img: '5.jpg' }
      ]
    }
  },
  components: {
    AppHeader,
    AppFooter,
    AppSlider
  }
}
</script>
