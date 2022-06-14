
$(document).ready(function(){
    $("p").click(function(){
        $("p").css({"background-color": "#fff","color" : "black"})
      $(this).css({"background-color": "blue","color" : "#fff"});
      $(".question").html($(this).text())
    });
    $(".answer").click(function(){
        $(".answer").css({"background-color": "#fff","color" : "black"})
      $(this).css({"background-color": "blue","color" : "#fff"});

    });
    $("#register").click(function(){
        $(".register").css("align-items","flex-end")
        $(".background").css({"right":"0","left":"auto"})
        $(".register").css("height","750px")
        $(".reg").css("display","block")
        $(".log").css("display","none")
        $(this).css("color","#fff")
        $("#login").css("color","black")


    });
    $("#login").click(function(){
          $(".register").css("align-items","flex-start")
          $(".background").css("left","0")
          $(".register").css("height","400px")
         $(".reg").css("display","none")
         $(".log").css("display","block")
        $(this).css("color","#fff")
        $("#register").css("color","black")


          
    })
     $(".register-btn").click(function(){
         $(".main-reg").css("display","block")
})
$(".fa-xmark").click(function(){
  $(".main-reg").css("display","none")
})
  //   $(".section-reg").click(function(){
  //    $(".main-reg").css("display","none")
  //  });
  //  $(".main-reg").click(function(){
  //   $(this).css("display","none")
  // });
  // $(".regster").click(function(){
  //   $("main-reg").css("display","block")
  // })
      
  });


