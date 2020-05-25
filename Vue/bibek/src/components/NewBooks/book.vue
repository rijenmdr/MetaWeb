<template xmlns="http://www.w3.org/1999/html">

    <div class="col-md-6 mt-3">
    <div class="card text-center">
        <div class="card-header bg-dark text-white">
            <h3>{{book.title}}</h3>
        </div>
        <div class="card-body">
            <h4 class="card-title">$65.12/month</h4>
            <p>{{book.description}}</p>
            <ul class="list-group">
                <li class="list-group-item">
                    Auhtor : {{book.author}}
                </li>
                <li class="list-group-item">
                    Created Date : {{book.created_date}}
                </li>
                <li class="list-group-item">
                    Added-By : {{book.added_by}}
                </li>
                <li class="list-group-item">
                    <div class="">
                        <div class="panel panel-success">
                            <div class="panel-heading">

                            </div>
                            <div class="panel-body qty">
                                <div class="pull-left">
                                    <input
                                            type="number"
                                            class="form-control"
                                            placeholder="Quantity"
                                            v-model="quantity"

                                    >

                                </div>
                                <div class="pull-right">
                                    <button class="btn btn-danger">{{quantity}}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>


            </ul>
            <a href="#" class="btn btn-success btn-block mt-2">Get Book</a>
        </div>
        <div class="card-footer text-muted">One Year Plan</div>
    </div>
    </div>
</template>

<script>
    export default  {
        props:['book'],
        data(){
            return {
                quantity:'Quantity'
            }
        },
        methods:{
            buyStock(){
                const order={
                    stockId : this.stock.id,
                    stockPrice: this.stock.price,
                    quantity: +this.quantity
                }
                this.$store.dispatch('buyStock',order);
                this.quantity = 0;
            }
        }

    }
</script>
<style>
    .qty{
        display: flex;
        justify-content: space-around;
    }
</style>