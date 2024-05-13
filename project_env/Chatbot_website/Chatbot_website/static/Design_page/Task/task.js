
let done = document.querySelectorAll(".fw-normal .done");
let remove = document.querySelectorAll(".fw-normal .remove");
let rows = document.querySelectorAll(".fw-normal");
let alertDone = document.querySelector(".alert-done");
let alertDelete = document.querySelector(".alert-delete");
let alertNoTask = document.querySelector(".alert-no");
let tableTask = document.querySelector("table")
let rl = rows.length;
if (rl === 0) {
  tableTask.classList.add('d-none');
  alertNoTask.classList.remove('d-none')
} 
for (let index = 0; index < done.length; index++) {
  done[index].onclick = ()=> removeTask(done[index],index);
  remove[index].onclick = ()=> removeTask(remove[index],index);
}


function removeTask(btn,rowIndex) {
  if(btn.classList[0]=='done'){
    alertDone.classList.remove('d-none')
  }else{
    alertDelete.classList.remove('d-none')
  }
  rows[rowIndex].classList.add('d-none');
  rl--;
  if (rl === 0) {
    tableTask.classList.add('d-none');
    setTimeout(() => {
      alertDelete.classList.add('d-none')
      alertDone.classList.add('d-none')
      alertNoTask.classList.remove('d-none')
    }, 1500);
  }  
  setTimeout(() => {
    alertDone.classList.add('d-none');
    alertDelete.classList.add('d-none');
  }, 2000);
}


