<template>
  <div id="app">
    <div>
      <router-link to="/login">Login</router-link><br>
      <router-link to="/register">Register</router-link>
      </div>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'app'
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
