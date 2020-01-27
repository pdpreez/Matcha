<template>
    <div>
        <h1>Register</h1>
        Username: <input v-model="username" type="text" placeholder="Username"/><br/>
        Email: <input v-model="email" type="text" placeholder="Email"/><br/>
        Password: <input v-model="password" type="password" placeholder="Password"/><br/>
        Confirm Password: <input v-model="confirm_password" type="password" placeholder="Confirm password"/><br/>
        <input type="submit" value="Register" v-on:click="submit()"/>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Register",
    data() {
        return {
            username: "newguy",
            email: "fake@email.fake",
            password: "P@ssword1",
            confirm_password: ""
        }
    },
    methods:
    {
        submit: function() {
            const form = {
                "username": this.username,
                "email": this.email,
                "password": this.password
            };
            axios.post("http://localhost:5000/register", form)
                    .then(function(response){
                        if (response.status == 201)
                        {
                            console.log("user created");
                        }
                    })
                    .catch(function(error){
                        console.log(error);
                        console.log("bad");
                    })
        }
    }
}
</script>