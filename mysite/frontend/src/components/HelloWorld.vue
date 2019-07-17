<template>
  <div class="hello">
    <div>
      <center>
        <h2>Registration Form</h2>
        <input type="text" v-model="name" name="name"  placeholder="Name">
        <br><br>
        <input type="email" v-model="email" name="email" @keypress="validEmail" placeholder="Email">
        <span v-if="!emailSuccess && email.length > 2"><br>Email not valid</span>
        <br><br>
        <input type="password" v-model="password" name="password" @keypress="validPassword" placeholder="Password">
        <span v-if="!passSuccess && password.length > 2"><br>Password not valid</span>
        <br><br>
        <input type="text" v-model="usertype" name="usertype" placeholder="UserType">
        <br><br>
        <button type="submit" @click="register">Resgiter</button>
      </center>
    </div>
  </div>
</template>

<script>

import axios from 'axios';


export default {
  name: 'HelloWorld',
  data () {
    return {
      name: '',
      email: '',
      password: '',
      usertype: '',
      emailSuccess: false,
      passSuccess: false,
      nameSuccess: false,
      usertypeSuccess: false,
    }
  },
  computed: {

  },
  methods: {
    register() {
        console.log("register called")
        axios
          .post("http://localhost:8000/polls/register/", {
            name: this.name,
            email: this.email,
            password: this.password,
            usertype: this.usertype
          })
          .then(res => {
            console.log(res);
            
          })
          .catch(err => {
            console.log("error");
          });
    },
    validEmail() {
      const re = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;      
      if(re.test(this.email)) {
         this.emailSuccess = true;
      } else {
        this.emailSuccess = false;
      }
    },
    validPassword() {
      const re = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
      if(re.test(this.password)) {
        this.passSuccess = true;
      } else {
        this.passSuccess = false;
      }
    },
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello{
  background-color: bisque;
}
</style>
