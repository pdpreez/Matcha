<template>
<div>
<h1>Login</h1>
    <form>
        Email: <input v-model="email" type="text" placeholder="email"/><br/>
        Password: <input v-model="password" type="password" placeholder="password"/><br/>
        <input type="button" value="Login" v-on:click="submit()"/>
    </form>
    <router-view name="login"/>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: "login",
    data() {
        return {
            email: "test@email.com",
            password: "P@ssword1"
        }
    },
    methods:
    {
        submit: function() {
            const form = {
                "email": this.email,
                "password": this.password
            };
            const self = this;
            axios.post("http://localhost:5000/login", form, {withCredentials: true})
                    .then(function(response){
                        if (response.status == 200)
                        {
                            self.$router.push({path: "/"})
                        }
                    })
                    .catch(function(error){
                        console.log(error)
                        console.log("bad bad")
                    })
        }
    }
}
</script>