let sign = document.querySelector(".login .sign .btn");
let login = document.querySelector(".login .log .btn");
let loginPage = document.querySelector(".login .login-form");
let signPage = document.querySelector(".login .sign-form");

let container = document.querySelector(".login .container");
let beforeContainer = window.getComputedStyle(container, '::before');



login.onclick = function(){
  // container.style.setProperty('--before','slide-reverse 1s ease-in-out forwards');
  // login.parentElement.classList.add("d-none");
  // sign.parentElement.classList.remove("d-none");
  // signPage.classList.add("d-none");
  // loginPage.classList.remove("d-none");
  window.addEventListener('resize', getWindowSize(0));
}
sign.onclick = function(){
  // container.style.setProperty('--before','slide 1s ease-in-out forwards')
  // sign.parentElement.classList.add("d-none");
  // login.parentElement.classList.remove("d-none");
  // loginPage.classList.add("d-none");
  // signPage.classList.remove("d-none");
  window.addEventListener('resize', getWindowSize(1));
}

// Function to get window size
function getWindowSize(e) {
  var windowWidth = window.innerWidth;
  if(e==0){
    login.parentElement.classList.add("d-none");
    sign.parentElement.classList.remove("d-none");
    signPage.classList.add("d-none");
    loginPage.classList.remove("d-none");
  }else{
    sign.parentElement.classList.add("d-none");
    login.parentElement.classList.remove("d-none");
    loginPage.classList.add("d-none");
    signPage.classList.remove("d-none");
  }
  if(windowWidth<=576 && e==0){
    container.style.setProperty('--before','slide-top 1s ease-in-out forwards')
  }else if(windowWidth<=576 && e==1){
    container.style.setProperty('--before','slide-bottom 1s ease-in-out forwards');
  }else if(windowWidth>576 && e==0){
    container.style.setProperty('--before','slide-reverse 1s ease-in-out forwards')
    
  }else if(windowWidth>576 && e==1){
    container.style.setProperty('--before','slide 1s ease-in-out forwards')

  }
}

// Call getWindowSize when the page loads
// getWindowSize();

// Add event listener for window resize
