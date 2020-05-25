<template>
    <section id="login ">
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-6 mx-auto">
                    <div class="card">
                        <div class="card-header">
                            <h4>Account Login</h4>
                        </div>
                        <div class="card-body">

                                <div class="form-group">
                                    <label for="name">Username</label>
                                    <input v-model="username" type="text" class="form-control">
                                </div>
                                <div class="form-group">
                                    <label for="name">password</label>
                                    <input v-model="password" type="password"  class="form-control">
                                </div>
                                <input @click="submit" type="submit" value="Submit" class="btn btn-success btn-block">

                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
</template>

<script>
    import axios from 'axios'
    export default{
        data(){
            return{
                username:'',
                password:''
            }
        },
        methods:{
          async submit(event) {
                event.preventDefault()
               await this.$store.dispatch('setToken', {username: this.username, password: this.password})
                console.log("hello")
                this.$router.push('/')

            }
        }

    }
</script>