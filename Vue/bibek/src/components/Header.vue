<template>
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
        <div class="container">
            <a href="index.html" class="navbar-brand">Books</a>
            <button
                    class="navbar-toggler"
                    data-toggle="collapse"
                    data-target="#navbarcollapse"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarcollapse">
                <ul class="navbar-nav ml-auto">
                    <router-link tag="li" active-class="nav-item active" to="/" exact><a class="nav-link">Home</a></router-link>
                    <router-link tag="li" active-class="nav-item active" to="/newbooks"><a class="nav-link">New Books</a></router-link>
                    <router-link tag="li" active-class="nav-item active" to="/login"><a class="nav-link">Login</a></router-link>
                    <router-link tag="li" active-class="nav-item active" to="/signup"><a class="nav-link">Sign-Up</a></router-link>

                </ul>
            </div>
        </div>
    </nav>
</template>