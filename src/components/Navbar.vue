<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
<!--    <a class="navbar-brand" href="#">Navbar</a>-->
    <router-link class="navbar-brand text-style"  to="/">VIETPHQ & VUE FLASK MYSQL & SAKILA</router-link>
<!--    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">-->
<!--      <span class="navbar-toggler-icon"></span>-->
<!--    </button>-->
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
<!--          <a class="nav-link active" aria-current="page" href="#">Home</a>-->
          <router-link class="btn btn-primary " aria-current="page" to="/">HOME</router-link>
        </li>
        <li class="nav-item">
<!--          <a class="nav-link" href="#">Features</a>-->
          <router-link class="btn btn-primary " aria-current="page" to="/actorshome">ACTORS</router-link>
        </li>
        <li class="nav-item">
          <router-link class="btn btn-primary " aria-current="page" to="/filmshome">FILMS</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>
.text-style{
  font-size: 30px !important;
  font-family: fantasy !important;
  color: brown !important;
}
.btn-primary{
  margin-left: 10px !important;
  color: brown !important;
  background: aliceblue !important;
}
</style>