<template>
  <div class="v-popup padding" >
    <div class="v-popup_header">
      <main class="form-HomeWork">
        <form>
          <span>
            <i class="material-icons" @click="closeHomeWork">close</i>
          </span><br><br>
          <h1 v-for="item in homework" v-bind:key="item">
            {{ item.title }}
          </h1>
          <p class="h3 mb-3 fw-normal" v-for="item in homework" v-bind:key="item">
            {{ item.work_text }}
          </p>
          <p class="date-icon" v-for="item in homework" v-bind:key="item">
            {{ item.pub_date }}
          </p>
          <p class="h3 mb-3 fw-normal" v-for="item in homework" v-bind:key="item">
            {{ item.comment }}
          </p>
          <button class="w-100 btn btn-lg btn-primary" type="submit" value="download" v-for="item in homework" v-bind:key="item">
            {{ item.home_work_file }}
          </button>
          <p class="datetime" v-for="item in homework" v-bind:key="item">
            {{ item.finished_date }}
          </p>
        </form>
      </main>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeWork',
  data () {
    return {
      homework: {
        title: '',
        work_text: '',
        comment: '',
        pub_date: '',
        finished_date: '',
        home_work_file: ''
      }
    }
  },
  mounted () {
    axios.get('http://localhost:8000/home-work/home-work/', {
      title: this.homework.title,
      work_text: this.homework.work_text,
      comment: this.homework.comment,
      pub_date: this.homework.pub_date,
      finished_date: this.homework.finished_date,
      home_work_file: this.homework.home_work_file
    }).then(response => {
      this.homework = response.data//   .then(response => {
      console.log('data: ')
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', 'file.txt')
      document.body.appendChild(link)
      link.click()
    })
  },
  methods: {
    closeHomeWork () {
      this.$emit('closeHomeWork')
    }
    // putFile () {
    //   axios.post('http://localhost:8000/home-work/home-work/', {
    //     home_work_file: this.files.home_work_file
    //   }).then(response => {
    //     this.files = response.data
    //     alert('так держать')
    //   })
    //     .catch(response => {
    //       alert('файл весит больше 2mb')
    //     })
    // }
  }
}
</script>
