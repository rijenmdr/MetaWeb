<template>
    <section id="posts">
      <div class="container">
        <div class="row">
          <div class="col-md-9">
            <div class="card">
              <div class="card-header">
                <h4>Latest Posts</h4>
              </div>
              <table class="table table-striped">
                <thead class="thead-dark">
                  <tr>
                    <th>#</th>
                    <th>Title</th>
                    <th>Category</th>
                    <th>Date</th>
                    <th></th>
                  </tr>
                  <tbody>
                    <tr>
                      <th>1</th>
                      <th>Post One</th>
                      <th>Designer</th>
                      <th>23-20</th>
                      <th>
                        <a href="details.html" class="btn btn-secondary">
                          <i class="fas fa-angle-double-right"></i>Details
                        </a>
                      </th>
                    </tr>
                    <tr>
                      <th>2</th>
                      <th>Post Two</th>
                      <th>Accountant</th>
                      <th>5-20</th>
                      <th>
                        <a href="details.html" class="btn btn-secondary">
                          <i class="fas fa-angle-double-right"></i>Details
                        </a>
                      </th>
                    </tr>
                    <tr>
                      <th>3</th>
                      <th>Post Three</th>
                      <th>Manager</th>
                      <th>11-20</th>
                      <th>
                        <a href="details.html" class="btn btn-secondary">
                          <i class="fas fa-angle-double-right"></i>Details
                        </a>
                      </th>
                    </tr>
                    <tr>
                      <th>4</th>
                      <th>Post Four</th>
                      <th>Business</th>
                      <th>2-20</th>
                      <th>
                        <a href="details.html" class="btn btn-secondary">
                          <i class="fas fa-angle-double-right"></i>Details
                        </a>
                      </th>
                    </tr>
                    <tr>
                      <th>5</th>
                      <th>Post Five</th>
                      <th>CTO</th>
                      <th>3-20</th>
                      <th>
                        <a href="details.html" class="btn btn-secondary">
                          <i class="fas fa-angle-double-right"></i>Details
                        </a>
                      </th>
                    </tr>
                  </tbody>
                </thead>
              </table>
            </div>
          </div>
          <div class="col-md-3">
              <div class="card text-center bg-primary text-white mb-3">
                  <div class="card-body">
                    <h3>My Website</h3>
                    <h4 class="display-4"> 
                      <i class="fas fa-pencil-alt"></i>1
          
                    </h4>
                    <router-link class="btn btn-outline-light btn-sm" to="/createWebsite">Create</router-link>
                 
                  </div>
              </div>
              <div class="card text-center bg-success text-white mb-3">
                <div class="card-body">
                  <h3>Edit</h3>
                  <h4 class="display-4"> 
                   <i class="fas fa-edit"></i>
        
                  </h4>
                <a href="categories.html" class="btn btn-outline-light btn-sm">edit</a>
                </div>
            </div>
            <div class="card text-center bg-warning text-white mb-3">
              <div class="card-body">
                <h3>Customer Feedback</h3>
                <h4 class="display-4"> 
                  <i class="fas fa-folder"></i>3
      
                </h4>
              <a href="user.html" class="btn btn-outline-light btn-sm">See more</a>
              </div>
          </div>
          </div>
        </div>
      </div>
    </section>
</template>