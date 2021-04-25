<template>
  <div class="wrapper">
    <div class="AppSliderItem" :style="{ 'margin-left': '-' + (100 * currentSlideIndex) + '%' }">
      <AppSliderItem
        v-for="item in slider_data"
        :key="item.id"
        :item_data="item"
      />
    </div>
  </div>
</template>

<script>
import AppSliderItem from '@/components/AppSliderItem'

export default {
  name: 'AppSlider',
  components: {
    AppSliderItem
  },
  props: {
    slider_data: {
      type: Array,
      default: () => []
    },
    interval: {
      type: Number,
      default: 0
    }
  },
  data () {
    return {
      currentSlideIndex: 0
    }
  },
  methods: {
    prevSlide () {
      if (this.currentSlideIndex > 0) {
        this.currentSlideIndex--
      }
    },
    nextSlide () {
      if (this.currentSlideIndex >= this.slider_data.length - 1) {
        this.currentSlideIndex = 0
      } else {
        this.currentSlideIndex++
      }
    }
  },
  mounted () {
    if (this.interval > 0) {
      const vm = this
      setInterval(function () {
        vm.nextSlide()
      }, vm.interval)
    }
  }
}
</script>

<style lang="scss">
  .wrapper {
    max-width: 750px;
    overflow: hidden;
    margin: 0 auto
  }
  .AppSliderItem {
    display: flex;
    transition: all ease .5s
  }
</style>
