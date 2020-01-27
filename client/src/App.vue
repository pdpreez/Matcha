<template>
  <div id="app">
    <login/>
    <register/>
  </div>
</template>

<script>
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'

export default {
  name: 'app',
  components: {
    Login,
    Register
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
