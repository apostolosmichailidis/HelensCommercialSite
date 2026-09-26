document.addEventListener("DOMContentLoaded",()=>{
  const t=document.querySelector(".menu-toggle"),n=document.querySelector("nav.main");
  if(t&&n)t.addEventListener("click",()=>{n.classList.toggle("open");t.setAttribute("aria-expanded",n.classList.contains("open"))});
  const y=document.getElementById("year");if(y)y.textContent=new Date().getFullYear();
});
