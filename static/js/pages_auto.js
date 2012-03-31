
foc_sid = 1;
var foc_t2_ttl = "Auto Calculators";
var foc_t2_fil = "auto-calculator.html"
var foc_pg = "";

var auto_page_ar = [
   ["car-affordability-calculator.html","Affordability Range","Car Affordability Calculator"],
   ["car-buying-calculator.html","Buying Cost Comparisons","Car Buying Calculator"],
   ["auto-loan-comparison-calculator.html","Car Loan Comparisons","Auto Loan Comparison Calculator"],
   ["car-depreciation-calculator.html","Depreciation Costs - Critical!","Car Depreciation Calculator"],
   ["car-down-payment-calculator.html","Down Payment Comparisons","Car Down Payment Calculator"],
   ["auto-loan-payoff-calculator.html","Early Payoff Savings","Auto Loan Payoff Calculator"],
   ["fuel-mileage-calculator.html","Fuel Mileage Savings","Fuel Mileage Calculator"],
   ["automobile-lease-calculator.html","Lease Payment with Breakdown","Automobile Lease Calculator"],
   ["car-lease-vs-buy-calculator.html","Lease Vs Buy Comparisons","Car Lease Vs Buy Calculator"],
   ["automobile-loan-payment-calculator.html","Loan Payments (required work hours!)","Automobile Loan Payment Calculator"],
   ["refinance-auto-loan-calculator.html","Refinance Net-Consequences","Refinance Auto Loan Calculator"],
   ["automobile-finance-calculator.html","Total Purchase Costs (Upside Down?)","Automobile Finance Calculator"]
];

   var v_file = document.location.href;
   var dom_ar = v_file.split("//");
   var url_ar = dom_ar[1].split("/");

   if(url_ar[1].indexOf("#") > -1) {
      var fil_ar = url_ar[1].split("#");
      foc_pg = fil_ar[0];
   } else {
      foc_pg = url_ar[1];
   }

   if(foc_pg != foc_t2_fil) {

      var v_auto_list = "<ul>";

      for(var pp = 0; pp<auto_page_ar.length; pp++) {

         if(foc_pg == auto_page_ar[pp][0]) {
            var foc_t3_ttl = auto_page_ar[pp][2];
            v_auto_list += "<li> " + auto_page_ar[pp][1] + "</li>";
         } else {
            v_auto_list += "<li> <a href='" + auto_page_ar[pp][0] + "'>" + auto_page_ar[pp][1] + "</a></li>";
         }

      }

      v_auto_list += "</ul>";

      foc_crumbs = "<div class='breadcrumbs'><a href='http://www.free-online-calculator-use.com/index.html'>Home</a> > "; 
      foc_crumbs += "<a href='http://www.free-online-calculator-use.com/" + foc_t2_fil + "'>" + foc_t2_ttl + "</a> > ";
      foc_crumbs += "" + foc_t3_ttl + "</div>";

   } else {

      foc_crumbs = "<div class='breadcrumbs'><a href='http://www.free-online-calculator-use.com/index.html'>Home</a> > "; 
      foc_crumbs += "" + foc_t2_ttl + "</div>";
   }
