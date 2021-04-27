<template>
  <div class="v-popup padding" >
    <div class="v-popup_header">
      <main class="form-HomeWork">
        <form>
          <span>
            <i class="material-icons" @click="closeFinishedHomeWork">close</i>
          </span><br><br>
          <h1 v-for="item in homework" v-bind:key="item">
            {{ item.title }}
          </h1>
          <p class="h3 mb-3 fw-normal" v-for="item in homework" v-bind:key="item">
            {{ item.home_work }}
          </p>
          <p class="date-icon" v-for="item in homework" v-bind:key="item">
            {{ item.created }}
          </p>
          <button class="w-100 btn btn-lg btn-primary" type="submit" value="download" v-for="item in homework" v-bind:key="item">
            {{ item.home_work_file }}
          </button>
          <p class="h3 mb-3 fw-normal" v-for="item in homework" v-bind:key="item">
            {{ item.mark }}
          </p>
          <p class="h3 mb-3 fw-normal" v-for="item in homework" v-bind:key="item">
            {{ item.comment_of_mark }}
          </p>
        </form>
      </main>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'FinishedHomeWork',
  data () {
    return {
      homework: {
        title: '',
        home_work: '',
        created: '',
        mark: '',
        comment_of_mark: ''
      },
      files:
          { finished_home_work_file: '' }
    }
  },
  mounted () {
    axios.get('http://localhost:8000/home-work/finished-home-work/', {
      title: this.homework.title,
      home_work: this.homework.home_work,
      created: this.homework.created,
      mark: this.homework.mark,
      comment_of_mark: this.homework.comment_of_mark
    }).then(response => {
      this.homework = response.data//   .then(response => {
      console.log('data: ')
    })
  },
  methods: {
    closeFinishedHomeWork () {
      this.$emit('closeFinishedHomeWork')
    },
    putFile () {
      axios.post('http://localhost:8000/home-work/finished-home-work/', {
        home_work_file: this.files.home_work_file
      }).then(response => {
        this.files = response.data
        alert('так держать')
      })
        .catch(response => {
          alert('файл весит больше 2mb')
        })
    }
  }
}
</script>
