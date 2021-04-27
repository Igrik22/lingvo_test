<template>
  <header>
    <table class="all">
      <tr>
        <td>
          <p>LINGVO</p>
          <span>English for dummies</span>
        </td>
        <td>
          <button class="btn" type="button" @click="goHomeWork">
            Home Work
          </button>
          <HomeWork v-if="isHomeWorkVisible" @closeHomeWork="closeHomeWork"/>
        </td>
        <td>
          <button class="btn" type="button" @click="goFinishedHomeWork">
            Tests for you
          </button>
          <FinishedHomeWork v-if="isFinishedHomeWorkVisible" @closeFinishedHomeWork="closeFinishedHomeWork"/>
        </td>
        <td>
            <input type="button" value="rus">
        </td>
        <td class="right-col">
          <button class="button4" @click="goLogin">Login</button>
          <Login v-if="isLoginVisible" @closeLogin="closeLogin"/>
        </td>
        <td class="right-col">
          <button class="button4" @click="goRegister">Register</button>
          <register v-if="isRegisterVisible" @closeRegister="closeRegister"/>
        </td>
      </tr>
    </table>
    <div class="window">
      WELCOME <br>
      This resource is intended for learning a foreign language
    </div>
  </header>
</template>

<script>
import Login from '@/components/Login'
import register from '@/components/register'
import HomeWork from '@/components/HomeWork'
import FinishedHomeWork from '@/components/FinishedHomeWork'

export default {
  name: 'AppHeader',
  components: {
    register,
    Login,
    HomeWork,
    FinishedHomeWork
  },
  data () {
    return {
      isLoginVisible: false,
      isRegisterVisible: false,
      isHomeWorkVisible: false,
      isFinishedHomeWorkVisible: false
    }
  // computed: {
  //   auth () {
  //     if (sessionStorage.getItem('auth-token')) {
  //       return true
  //     } else {
  //       return 'incorrect data'
  //     }
  //   }
  },
  methods: {
    goLogin () {
      this.isLoginVisible = true
    },
    closeLogin () {
      this.isLoginVisible = false
    },
    goRegister () {
      this.isRegisterVisible = true
    },
    closeRegister () {
      this.isRegisterVisible = false
    },
    goHomeWork () {
      this.isHomeWorkVisible = true
    },
    closeHomeWork () {
      this.isHomeWorkVisible = false
    },
    goFinishedHomeWork () {
      this.isFinishedHomeWorkVisible = true
    },
    closeFinishedHomeWork () {
      this.isFinishedHomeWorkVisible = false
    }
  }
}
</script>

<style lang="scss" media="screen">
  header p {
    font-size: 350%;
    color: green;
    text-decoration-skip-ink: inherit;
    text-decoration-color: green;
    padding: 1px;
    margin: 1px;
  }
  header span {
    font-size: 100%;
    color: green;
    text-decoration-skip-ink: inherit;
    text-decoration-color: green;
    padding: 1px;
    margin: 1px;
   }
  .window {
    background: -webkit-gradient(linear, 5 5, 5 70%, from(#00BBD6), to(#EBFFFF));
    font-size: 200%;
    color: red;
    padding: 1px;
    text-align: center;
    }
  table.all {
    width:  100%; /* Ширина таблицы */
    border-bottom-width: revert; /* Расстояние между ячейками */
  }
  table.all td {
    width: 100%; /* Ширина ячеек */
    vertical-align: top; /* Выравнивание по верхнему краю */
   }
  td button.btn {
   font-family: Arial, Helvetica, sans-serif;
   font-size: 14px;
   width: 130px;
   height: 40px;
   float: left;
   background: -webkit-gradient(linear, left top, left bottom, from(lightpink),
     color-stop(0.78, antiquewhite), to(antiquewhite));
   border-radius: 14px;
   outline: none;
   border: none;
   margin: 30px;
  }
  td button.btn:hover {
    box-shadow: inset 0 -1px 1px rgba(0,0,0,0), inset 0 1px 2px rgba(0,0,0,0), inset 0 0 0 60px rgba(255,255,0,.5);
  }
   td button.btn:active {
    border-color: rgba(177, 159, 0, 1);
    box-shadow: inset 0 -1px 1px rgba(0, 0, 0, .1), inset 0 1px 2px rgba(0, 0, 0, .3), inset 0 0 0 60px rgba(255, 255, 0, .45);
  }
  td button:hover {
    box-shadow: inset 0 -1px 1px rgba(0,0,0,0), inset 0 1px 2px rgba(0,0,0,0), inset 0 0 0 60px rgba(255,255,0,.5);
  }
  td button:active {
    border-color: rgba(177, 159, 0, 1);
    box-shadow: inset 0 -1px 1px rgba(0, 0, 0, .1), inset 0 1px 2px rgba(0, 0, 0, .3), inset 0 0 0 60px rgba(255, 255, 0, .45);
  }
  td input {
    text-align: center;
    line-height: normal;
    font-family: Montserrat,Verdana,sans-serif;
    list-style: initial;
    font-size: 10px;
    padding: 12%;
    position: marker;
    border-radius: 50%;
    outline: none;
    border: none;
    color: darkblue;
    background: rebeccapurple;
    margin: 30px;
   }
  td input:hover {
    box-shadow: inset 0 -1px 1px rgba(0,0,0,0), inset 0 1px 2px rgba(0,0,0,0), inset 0 0 0 60px rgba(255,255,0,.5);
  }
  td input:active {
    border-color: rgba(177,159,0,1);
    box-shadow: inset 0 -1px 1px rgba(0,0,0,.1), inset 0 1px 2px rgba(0,0,0,.3), inset 0 0 0 60px rgba(255,255,0,.45);
  }
  .button4  {
    display: inline-block;
    color: black;
    font-size: 80%;
    font-weight: 780;
    text-decoration: none;
    user-select: none;
    padding: .24em .78em;
    outline: none;
    border: 1px solid rgb(250,172,17);
    border-radius: 10px;
    background: rgb(255,212,3) linear-gradient(rgb(255,212,3), rgb(248,157,23));
    box-shadow: inset 0 -2px 1px rgba(0,0,0,0), inset 0 1px 2px rgba(0,0,0,0), inset 0 0 0 60px rgba(255,255,0,0);
    transition: box-shadow .2s, border-color .2s;
  }
  a.button4:hover {
    box-shadow: inset 0 -1px 1px rgba(0,0,0,0), inset 0 1px 2px rgba(0,0,0,0), inset 0 0 0 60px rgba(255,255,0,.5);
  }
  a.button4:active {
    border-color: rgba(177,159,0,1);
    box-shadow: inset 0 -1px 1px rgba(0,0,0,.1), inset 0 1px 2px rgba(0,0,0,.3), inset 0 0 0 60px rgba(255,255,0,.45);
  }
  header {
    position: marker; /* Фиксированное положение */
    left: auto; /* Левый нижний угол */
    padding: 1px; /* Поля вокруг текста */
    background: #00BBD6; /* Цвет фона */
    color: midnightblue; /* Цвет текста */
    width: 100%;
    min-height: 90px;
  }
  .v-popup {
    margin-left: -180px;
    padding: 30px;
    position: absolute;
    align-items: center;
    top: 100px;
    background: gray;

    &__header {
      display: initial;
      justify-content: center;
      align-items: center;
      position: absolute;
      width: 200px;
    }

    input.form-control {
      display: compact;
      justify-content: center;
      align-items: center;
      background: yellow;
      border-radius: 14px;
      margin: 5px;
    }

    i {
      color: red;
    }

    input.w-100.btn.btn-lg.btn-primary {
      color: yellow;
      background: #00BBD6;
      display: compact;
      justify-content: center;
      align-items: center;
      margin: 2px;
    }
  }
  .v-popup.padding {
    margin-left: -400px;
    padding: 200px;
    position: absolute;
    align-items: center;
    top: 10px;
    background: gray;

    &__header {
      display: initial;
      justify-content: center;
      align-items: center;
      position: absolute;
      width: 200px;
    }
  }
</style>
