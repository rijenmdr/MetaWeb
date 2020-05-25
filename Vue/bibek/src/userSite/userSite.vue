<template>
    <div>
        <Header/>
        <Landing/>
        <Features/>
    </div>
</template>
<script>
import Header from './components/header'
import Landing from './components/landing'
import Features from './components/features'
export default {
    components:{
        Header,
        Landing,
        Features
    }
}
</script>