<template>
    <div class="container">
        <div class="row">
        <Book v-for="book in books" :book="book"></Book>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import Book from "./book";
    export default {
        data(){
            return{
                books:[]
            }
        },
        components:{
            Book,

        },
        computed:{
            stocks(){
                return this.$store.getters.stocks;
            }
        },
        created() {
            axios.get('http://127.0.0.1:8000/api/books',{
                headers: {
                    'Authorization': 'Bearer '+ this.$store.getters.getToken
                }
            })
            .then(res=>{
                this.books = res.data.data
            })
        }
    }
</script>