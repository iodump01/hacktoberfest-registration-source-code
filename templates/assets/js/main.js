// const header = document.querySelector("[data-header]");

// window.addEventListener("scroll", function () {
//   window.scrollY >= 1
//     ? header.classList.add("active")
//     : header.classList.remove("active");
// });

/**
 * go top
 */

const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {
  window.scrollY >= 500
    ? goTopBtn.classList.add("active")
    : goTopBtn.classList.remove("active");
});

const listItem = document.querySelectorAll(".list");

function activateLink() {
  listItem.forEach((item) => {
    item.classList.remove("active");
  });
  this.classList.add("active");
}

listItem.forEach((item) => {
  item.addEventListener("click", activateLink);
});

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("go_top_id").style.bottom = "0";
  } else {
    document.getElementById("go_top_id").style.bottom = "-150px";
  }
  prevScrollpos = currentScrollPos;
};

(function ($) {
  "use strict";

  /*PRELOADER JS*/
  $(window).on("load", function () {
    $(".atf-status").fadeOut();
    $(".atf-preloader").delay(350).fadeOut("slow");
  });
  /*END PRELOADER JS*/

  /*--------------------------------------------------------------
       Mobile Menu
      --------------------------------------------------------------*/

  $(".atf-nav").append('<span class="atf-menu-toggle"><span></span></span>');
  $(".menu-item-has-children").append(
    '<span class="atf-menu-dropdown-toggle"></span>'
  );
  $(".atf-menu-toggle").on("click", function () {
    $(this)
      .toggleClass("atf-toggle-active")
      .siblings(".atf-nav-list")
      .slideToggle();
  });
  $(".atf-menu-dropdown-toggle").on("click", function () {
    $(this).toggleClass("active").siblings("ul").slideToggle();
  });

  /*--------------------------------------------------------------
       One Page Navigation
      --------------------------------------------------------------*/
  // Click To Go Top
  $(".atf-smooth-move").on("click", function () {
    var thisAttr = $(this).attr("href");
    if ($(thisAttr).length) {
      var scrollPoint = $(thisAttr).offset().top - 50;
      $("body,html").animate(
        {
          scrollTop: scrollPoint,
        },
        800
      );
    }
    return false;
  });

  // One Page Active Class
  var topLimit = 300,
    ultimateOffset = 200;

  $(".atf-onepage-nav").each(function () {
    var $this = $(this),
      $parent = $this.parent(),
      current = null,
      $findLinks = $this.find("a");

    function getHeader(top) {
      var last = $findLinks.first();
      if (top < topLimit) {
        return last;
      }
      for (var i = 0; i < $findLinks.length; i++) {
        var $link = $findLinks.eq(i),
          href = $link.attr("href");

        if (href.charAt(0) === "#" && href.length > 1) {
          var $anchor = $(href).first();
          if ($anchor.length > 0) {
            var offset = $anchor.offset();
            if (top < offset.top - ultimateOffset) {
              return last;
            }
            last = $link;
          }
        }
      }
      return last;
    }

    $(window).on("scroll", function () {
      var top = window.scrollY,
        height = $this.outerHeight(),
        max_bottom = $parent.offset().top + $parent.outerHeight(),
        bottom = top + height + ultimateOffset;

      var $current = getHeader(top);

      if (current !== $current) {
        $this.find(".active").removeClass("active");
        $current.addClass("active");
        current = $current;
      }
    });
  });

  /*--------------------------------------------------------------
       Sticky Back To Top
      --------------------------------------------------------------*/

  $(window).on("scroll", function () {
    if ($(window).scrollTop() > 50) {
      $(".atf-sticky-header").addClass("atf-nav");
      $(".atf-back-to-top").addClass("open");
    } else {
      $(".atf-sticky-header").removeClass("atf-nav");
      $(".atf-back-to-top").removeClass("open");
    }
  });
  /*--------------------------------------------------------------
       START SCROLL UP
      --------------------------------------------------------------*/
  if ($(".atf-back-to-top").length) {
    $(".atf-back-to-top").on("click", function () {
      var target = $(this).attr("data-targets");
      // animate
      $("html, body").animate(
        {
          scrollTop: $(target).offset().top,
        },
        1000
      );
    });
  }

  /*--------------------------------------------------------------
         END SCROLL UP
      --------------------------------------------------------------*/

  /*--------------------------------------------------------------
       START PARTNER JS
      --------------------------------------------------------------*/
  $(".atf-brand-active").owlCarousel({
    margin: 5,
    autoplay: true,
    items: 3,
    loop: true,
    nav: false,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 3,
      },
      1000: {
        items: 4,
      },
    },
  });
  /*--------------------------------------------------------------
       END PARTNER JS
      --------------------------------------------------------------*/

  /*--------------------------------------------------------------
		START WOW SCROLL SPY
      --------------------------------------------------------------*/
  var wow = new WOW({
    //disabled for mobile
    mobile: false,
  });

  wow.init();
  /*--------------------------------------------------------------
		END WOW SCROLL SPY
      --------------------------------------------------------------*/

  /*--------------------------------------------------------------
		START PARALLAX JS
      --------------------------------------------------------------*/
  (function () {
    if (
      /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
        navigator.userAgent
      )
    ) {
    } else {
      $(window).stellar({
        horizontalScrolling: false,
        responsive: true,
      });
    }
  })();

  /*--------------------------------------------------------------
		END PARALLAX JS
      --------------------------------------------------------------*/


      //new register
  // $("#sign-up-form").submit(function (e) {
  //   e.preventDefault();
  //   let span = $('span#sub_icon')
  //   span.append("<i class='ms-2 fa fas fa-spinner fa-spin'></i>")
  //   let token = $("input#csrf").val();
  //   let name = $("input#RName").val();
  //   let email = $("input#REmail").val();
  //   let mobile = $("input#RMobile").val();
  //   let CollegeName = $("input#CollegeName").val();
  //   let DepartmentName = $("input#DepartmentName").val();
  //   let Class = $("#Class").find(":selected").val();
  //   let Promo = $("#Promo").find(":selected").val();
  //   let Address = $("input#Address").val();
  //   let myValue = {
  //     csrfmiddlewaretoken: token,
  //     name,
  //     email,
  //     mobile,
  //     CollegeName,
  //     DepartmentName,
  //     Class,
  //     Promo,
  //     Address
  //   };
  //   var saveData = $.ajax({
  //     type: "POST",
  //     url: "/submit",
  //     data: myValue,
  //     dataType: "text",
  //     success: function (resultData) {
  //       span.empty()
  //      alert(JSON.parse(resultData).Data)
  //     },
  //   });
  //   saveData.error(function (resultData) {
  //     span.empty()
  //     alert(JSON.parse(resultData).Error)
  //   });
  // });


  // Contact form submit
  $("#contactForm").submit(function (e) {
    e.preventDefault();
    let msg_span = $("span#msg_icon")
    msg_span.append("<i class='ms-2 fa fas fa-spinner fa-spin'></i>")
    let token = $("meta[name=token__]").attr("content");
    let name = $("input#name").val();
    let email = $("input#form_email").val();
    let subject = $("input#subject").val();
    let query = $("input#subject").val();
    let myValue = {
      csrfmiddlewaretoken: token,
      name,
      email,
      subject,
      query,
    };
    var saveData = $.ajax({
      type: "POST",
      url: "/ticket/message",
      data: myValue,
      dataType: "text",
      success: function (resultData) {
        msg_span.empty()
        $("div#formResult")
          .append(`<div class="alert alert-success alert-dismissible mt-2" role="alert">
        <strong>Success: </strong> ${JSON.parse(resultData).Data}
        <button type="button" class="close border-0 bg-transparent outline-none h4" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
      </div>`);
      },
    });
    saveData.error(function () {
      msg_span.empty()
      $(
        "div#formResult"
      ).append(`<div class="alert alert-danger alert-dismissible mt-2" role="alert">
        <strong>Fail: </strong> Something went wrong.
          <button type="button" class="close border-0 bg-transparent outline-none h4" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
      </div>`);
    });
  });
})(jQuery);
