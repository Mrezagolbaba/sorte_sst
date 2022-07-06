// counter
{(function () {
   const second = 1000,
      minute = second * 60,
      hour = minute * 60,
      day = hour * 24;
   
 
   let today = new Date(),
      dd = String(today.getDate()).padStart(2, "0"),
      mm = String(today.getMonth() + 1).padStart(2, "0"),
      yyyy = today.getFullYear(),
      nextYear = yyyy + 1,
      dayMonth = "08/01/",
      targetDay = dayMonth + yyyy;
   //end
   
   const countDown = new Date(targetDay).getTime(),
      x = setInterval(function() {    
      const now = new Date().getTime(),
      distance = countDown - now;
      
      document.getElementById("jday").innerText = Math.floor(distance / (day)),
      document.getElementById("jhour").innerText = Math.floor((distance % (day)) / (hour)),
      document.getElementById("jmin").innerText = Math.floor((distance % (hour)) / (minute)),
      document.getElementById("jsec").innerText = Math.floor((distance % (minute)) / second);

      document.getElementById("lday").innerText = Math.floor(distance / (day)),
      document.getElementById("lhour").innerText = Math.floor((distance % (day)) / (hour)),
      document.getElementById("lmin").innerText = Math.floor((distance % (hour)) / (minute)),
      document.getElementById("lsec").innerText = Math.floor((distance % (minute)) / second);

      document.getElementById("nday").innerText = Math.floor(distance / (day)),
      document.getElementById("nhour").innerText = Math.floor((distance % (day)) / (hour)),
      document.getElementById("nmin").innerText = Math.floor((distance % (hour)) / (minute)),
      document.getElementById("nsec").innerText = Math.floor((distance % (minute)) / second);
   })
}())};
// counteer ends

// pause video from play background
   {
      var vid = document.getElementById("myVideo");

      function pauseVid() {
         vid.pause();
      }
   }
// ends