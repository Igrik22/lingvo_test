<template>
  <div class="AppSliderItem">
    <img :src="require('../assets/' + item_data.img)">
  </div>
</template>

<script>
export default {
  name: 'AppSliderItem',
  props: {
    item_data: {
      type: Object,
      default: () => {}
    }
  }
}
</script>
