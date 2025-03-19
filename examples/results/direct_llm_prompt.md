can you Extract the Annualised Percentage Rate (”APR“) for me and output it as a table. 
loan_amount_list=[50000,1000000,2000000,3000000,5000000,800000,10000000,1500000] 
# loan amounts are 50,000, 100,000 200,000 300,000 500,000 800,000 1,000,000 1,500,000
period_list=[12,24,36,60] 
Example:
Loan Amount (HKD$) | 12 months | 24 months | 36 months | 60 months |
-|-|-|-|-
50,000|11.24%|11.24%|10.97%|10.3%|
...

when create the table, remember the Loan Amount (HKD$) column must match the loan_amount_list or loan amounts that are given, not a range.
Here is the html, extract from here:
<!DOCTYPE html><html class="js geolocation json svg checked template no-applicationcache audio audio-ogg audio-mp3 audio-opus audio-wav no-audio-m4a canvas canvastext hashchange history inputtypes-search inputtypes-tel inputtypes-url inputtypes-email no-inputtypes-datetime inputtypes-date inputtypes-month inputtypes-week inputtypes-time inputtypes-datetime-local inputtypes-number inputtypes-range inputtypes-color postmessage postmessage-structuredclones video no-video-ogg no-video-h264 no-video-h265 video-webm video-vp9 no-video-hls no-video-av1 webgl websockets cssanimations backgroundsize borderimage borderradius boxshadow csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox flexboxlegacy fontface generatedcontent cssgradients hsla multiplebgs opacity cssreflections rgba textshadow csstransforms supports csstransforms3d csstransitions localstorage sessionstorage websqldatabase svgclippaths inlinesvg smil webworkers arrow progressbar meter hidden details touchevents emoji notification placeholder bp--landscape ua-no-touch ua-windows grunticon bp--h-large" lang="en-US"><head><script src="https://rules.quantcount.com/rules-p-Mp998fWY2NSrV.js" async=""></script><script src="https://secure.quantserve.com/quant.js" async="" type="text/javascript"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=DC-13577761&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v78233097za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" src="https://cdn.taboola.com/scripts/eid.es5.js" charset="UTF-8" async="async"></script><script type="text/javascript" src="https://cdn.taboola.com/scripts/cds-pips.js" charset="UTF-8" async="async"></script><script async="" src="//cdn.taboola.com/libtrc/unip/1626789/tfa.js" id="tb_tfa_script"></script><script src="https://s.yimg.com/wi/ytc.js" async=""></script><script type="text/javascript" async="" src="https://snap.licdn.com/li.lms-analytics/insight.min.js"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=DC-6629002&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v78233097za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=DC-8134849&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v78233097za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=DC-9579696&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v78233097za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" async="" src="https://static.criteo.net/js/ld/ld.js"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=DC-8005120&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v78233097za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=DC-8744175&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v78233097za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=DC-6024809&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v78233097za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=G-YHRGW6LC0H&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v813165961za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/destination?id=G-KVFB5VQ149&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v813165961za200zb6381932&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719"></script><script src="https://connect.facebook.net/signals/config/1682745115305829?v=2.9.187&amp;r=stable&amp;domain=www.sc.com&amp;hme=9d6c2cc137748d003f279fac8d52b2defc993e1177ef802e0d5b230c72882031&amp;ex_m=71%2C123%2C108%2C112%2C62%2C4%2C101%2C70%2C16%2C98%2C90%2C51%2C55%2C177%2C180%2C192%2C188%2C189%2C191%2C29%2C102%2C53%2C78%2C190%2C172%2C175%2C185%2C186%2C193%2C134%2C41%2C198%2C195%2C196%2C34%2C147%2C15%2C50%2C202%2C201%2C136%2C18%2C40%2C1%2C43%2C66%2C67%2C68%2C72%2C94%2C17%2C14%2C97%2C93%2C92%2C109%2C52%2C111%2C39%2C110%2C30%2C95%2C26%2C173%2C176%2C144%2C87%2C57%2C85%2C33%2C74%2C0%2C96%2C32%2C28%2C83%2C84%2C89%2C47%2C46%2C88%2C37%2C11%2C12%2C13%2C6%2C7%2C25%2C22%2C23%2C58%2C63%2C65%2C76%2C54%2C103%2C27%2C77%2C9%2C8%2C81%2C48%2C21%2C105%2C104%2C106%2C99%2C10%2C20%2C3%2C38%2C75%2C19%2C5%2C91%2C82%2C44%2C35%2C86%2C2%2C36%2C64%2C42%2C107%2C45%2C80%2C69%2C113%2C61%2C60%2C31%2C100%2C59%2C56%2C49%2C79%2C73%2C24%2C114%2C137%2C168%2C203%2C205%2C245%2C171%2C229%2C124%2C162%2C149%2C156%2C132%2C242%2C118%2C204%2C129%2C130%2C150%2C178%2C164%2C120%2C243%2C170%2C121%2C139%2C125%2C159%2C152%2C200%2C115%2C131" async=""></script><script src="https://connect.facebook.net/signals/config/2777323578949015?v=2.9.187&amp;r=stable&amp;domain=www.sc.com&amp;hme=9d6c2cc137748d003f279fac8d52b2defc993e1177ef802e0d5b230c72882031&amp;ex_m=71%2C123%2C108%2C112%2C62%2C4%2C101%2C70%2C16%2C98%2C90%2C51%2C55%2C177%2C180%2C192%2C188%2C189%2C191%2C29%2C102%2C53%2C78%2C190%2C172%2C175%2C185%2C186%2C193%2C134%2C41%2C198%2C195%2C196%2C34%2C147%2C15%2C50%2C202%2C201%2C136%2C18%2C40%2C1%2C43%2C66%2C67%2C68%2C72%2C94%2C17%2C14%2C97%2C93%2C92%2C109%2C52%2C111%2C39%2C110%2C30%2C95%2C26%2C173%2C176%2C144%2C87%2C57%2C85%2C33%2C74%2C0%2C96%2C32%2C28%2C83%2C84%2C89%2C47%2C46%2C88%2C37%2C11%2C12%2C13%2C6%2C7%2C25%2C22%2C23%2C58%2C63%2C65%2C76%2C54%2C103%2C27%2C77%2C9%2C8%2C81%2C48%2C21%2C105%2C104%2C106%2C99%2C10%2C20%2C3%2C38%2C75%2C19%2C5%2C91%2C82%2C44%2C35%2C86%2C2%2C36%2C64%2C42%2C107%2C45%2C80%2C69%2C113%2C61%2C60%2C31%2C100%2C59%2C56%2C49%2C79%2C73%2C24%2C114" async=""></script><script async="" src="https://connect.facebook.net/en_US/fbevents.js"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-MPWTVNC&amp;l=dataLayer&amp;gtm=45He53d3v6381932za200&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887799"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-PRJSHV2&amp;l=dataLayer&amp;gtm=45He53d3v6381932za200&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887799"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-KVFB5VQ149%2CG-YHRGW6LC0H&amp;l=dataLayer&amp;cx=c&amp;gtm=45He53d3v6381932za200&amp;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887799"></script><script type="text/javascript" async="async" src="https://standchartbank.sc.omtrdc.net/b/ss/standchartbankprod/10/JS-2.23.0-LEWM/s09808529351423?AQB=1&amp;ndh=1&amp;pf=1&amp;callback=s_c_il[1].doPostbacks&amp;et=1&amp;t=18%2F2%2F2025%2010%3A49%3A37%202%20-480&amp;d.&amp;nsid=0&amp;jsonv=1&amp;.d&amp;sdid=252439CB8FDFD965-4657483F1F84AB3B&amp;mid=38067932791279137821799872934696471824&amp;aamlh=9&amp;ce=UTF-8&amp;ns=standchartbank&amp;cdp=2&amp;pageName=hk%3Aen%3Apersonal%3Aproduct%3Aloans%3Apersonal-loans%3Apersonal-instalment-loan%3Apersonal-instalment-loan&amp;g=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F&amp;c.&amp;getNewRepeat=3.0.1&amp;getTimeParting=6.3&amp;inList=3.0&amp;pt=3.0&amp;p_fo=3.0&amp;apl=4.0&amp;getValOnce=3.0.1&amp;getPreviousValue=3.0.1&amp;getQueryParam=4.0.1&amp;getPageLoadTime=2.0.2&amp;performanceWriteFull=1.0&amp;performanceWritePart=1.0&amp;performanceCheck=1.0&amp;getPercentPageViewed=5.0.2&amp;handlePPVevents=4.0&amp;.c&amp;h.&amp;architecture=x86&amp;bitness=64&amp;platformVersion=19.0.0&amp;.h&amp;cc=HKD&amp;ch=personal-loans&amp;server=www.sc.com&amp;events=event100&amp;aamb=6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y&amp;c1=D%3Dv1&amp;v1=hk%3Aen%3Apersonal%3Aproduct%3Aloans%3Apersonal-loans%3Apersonal-instalment-loan%3Apersonal-instalment-loan&amp;c2=D%3Dv2&amp;v2=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F&amp;v3=undefined&amp;c4=D%3Dv4&amp;v4=loans&amp;c5=D%3Dv5&amp;v5=personal-loans&amp;c6=D%3Dv6&amp;c7=D%3Dv7&amp;v7=hk&amp;c8=D%3Dv8&amp;v8=en&amp;v9=year%3D2025%20%7C%20month%3DMarch%20%7C%20date%3D18%20%7C%20day%3DTuesday%20%7C%20time%3D10%3A49%20AM&amp;v10=New&amp;v14=highestPercentViewed%3D%20%7C%20initialPercentViewed%3D&amp;c23=D%3Dmid&amp;v23=D%3Dmid&amp;v30=loans&amp;v42=product&amp;v63=personal-loans&amp;c75=2025-3-18%2010%3A49%3A37&amp;v84=personal-instalment-loan&amp;v88=loans%3Apersonal-loans%3A&amp;v89=loans%3Apersonal-loans&amp;v95=na&amp;s=1280x720&amp;c=24&amp;j=1.6&amp;v=N&amp;k=Y&amp;bw=1280&amp;bh=720&amp;mcorgid=B40014495C3466100A495EB8%40AdobeOrg&amp;AQE=1"></script>
	<meta http-equiv="X-UA-Compatible" content="IE=Edge">
	<meta charset="UTF-8">

	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-capable" content="yes">
	<link rel="profile" href="http://gmpg.org/xfn/11">
				<script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-PHQV2K"></script><script src="https://av.sc.com/assets/tpl/onetrust/production/hk/scripttemplates/otSDKStub.js" type="text/javascript" charset="UTF-8" data-domain-script="dcfcce45-805d-4309-a4b1-704b7638f2c9"></script>
<script type="text/javascript">
	function OptanonWrapper() { }
	</script>
<script>var implicitContent = true;</script>
		<script>var scAnalyticsDataArray=[];</script>
<script>var digitalData = {"page":{"pageInfo":{"pageID":8410,"pageName":"hk:en:personal:product:personal-loans::personal-instalment-loan:personal-instalment-loan"},"category":{"primaryCategory":"personal-loans","subCategory1":"","subCategory2":"personal-instalment-loan"},"attributes":{"language":"en","country":"hk","currency":"HKD"},"productInfo":{"productId":"Dummy","subProductId":"n\/a"}}};</script>
<script id="adobelaunchscript" src="//assets.adobedtm.com/launch-ENa7eb1ee509d342d08c584f8573a369b3.min.js"></script><script src="https://assets.adobedtm.com/extensions/EPbf7b42aa08bc4f10879b1484195e80d1/AppMeasurement.min.js" async=""></script><script src="https://assets.adobedtm.com/extensions/EPbf7b42aa08bc4f10879b1484195e80d1/AppMeasurement_Module_AudienceManagement.min.js" async=""></script><script>
window.pageHierarchyValue = (function () {
  // Function to retrieve cookie value by name
  function getCookieValue(name) {
      const cookieString = `; ${document.cookie}`;
      const parts = cookieString.split(`; ${name}=`);
      return parts.length === 2 ? decodeURIComponent(parts.pop().split(";").shift()) : "";
  }

  // Get 'pageHierarchy' from cookie
  let pageHierarchy = getCookieValue("pageHierarchy") || "";

  // Retrieve 'hier' from the query string or session storage
  const urlParams = new URLSearchParams(window.location.search);
  let hierValue = urlParams.get("hier") || sessionStorage.getItem("hier");

  // Parse URL components
  const { hostname, pathname } = window.location;
  const pathSegments = pathname.split("/").filter(Boolean); // Filter out empty strings

  // Define the domains to check
  const validDomains = ["sc.com", "preview.standardchartered.com", "standardchartered.com"];

  // Define pageHierarchy value based on hostname and path
  const isValidDomain = validDomains.some((domain) => hostname.includes(domain));
  if (isValidDomain && pathSegments[0] === "hk" && pathSegments.length === 1) {
      pageHierarchy = "home";
  } else {
      const lastSegment = pathSegments[pathSegments.length - 1];
      if (pageHierarchy === "home") {
          pageHierarchy = `home:${lastSegment}`;
      } else {
          pageHierarchy = pageHierarchy.length ? `${pageHierarchy}:${lastSegment}` : lastSegment;
      }
  }

  // Convert pageHierarchy into an array of segments
  let hierarchySegments = pageHierarchy.split(":");

  // Prepend the hierValue if it exists
  if (hierValue) {
      hierarchySegments.unshift(hierValue);
  }

  // Limit the hierarchy to the last 5 segments
  if (hierarchySegments.length > 5) {
      hierarchySegments = hierarchySegments.slice(-5);
  }

  // Update the 'pageHierarchy' cookie with the new value
if(document.location.host.includes("sc.com")){
    document.cookie = `pageHierarchy=${encodeURIComponent(hierarchySegments.join(":"))}; domain=.sc.com; path=/`;}
  else if(document.location.host.includes("standardchartered.com")){//added to cover UAT enviroment
    document.cookie = `pageHierarchy=${encodeURIComponent(hierarchySegments.join(":"))}; domain=.standardchartered.com; path=/`;
  }


  // Return the final hierarchy as a string
  return hierarchySegments.join(":");
})();
</script>

	<style>
		@media (min-width: 681px) and (max-width: 1023.98px) {
.sc-bnr-two-col .sc-bnr__bg-wrapper--no-overlay {
	position: relative !important;
    min-height: 300px !important;
}
.sc-bnr-product-variation .sc-bnr-cvp {
         text-align: center;
    }
}
.sc-bnr .sc-bnr__box{
padding-left:0px;
}

.sc-bnr-product-variation .sc-bnr__content--bg-transparent .sc-bnr-desc{
font-weight: 400 !important;
}
@media (max-width: 767.98px) {
.sc-pil-calculator__input-box {
   width: 70% !important;
}
}
.sc-bnr-product-variation .sc-bnr__content--bg-transparent .sc-bnr-buttons .sc-btn-arrow {
    text-decoration: underline;
    text-decoration-style: dashed;
    text-underline-offset: 3px;
}
		/* NOTE: This styles can't be in a external stylesheet due to browsers bug */
		.no-touchevents .hover-icon-with-gradient-blue-to-green:hover .hover-icon svg path {
			fill: url('#gradient-blue-to-green');
		}
	</style>
		
		<!-- Google Tag Manager -->
		<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
		new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
		j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
		'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
		})(window,document,'script','dataLayer','GTM-PHQV2K');</script>
		<!-- End Google Tag Manager -->
			<link rel="canonical" href="https://www.sc.com/hk/loans/personal-instalment-loan/"><title>Personal Instalment Loan | Interest rate as low as 1.85% | Hong Kong – Standard Chartered HK</title>
<meta name="robots" content="max-image-preview:large">
<link href="//www.google-analytics.com" rel="dns-prefetch" crossorigin="">
<link href="//www.google.com" rel="dns-prefetch" crossorigin="">
<link href="//stats.g.doubleclick.net" rel="dns-prefetch" crossorigin="">
<link href="//c.go-mpulse.net" rel="dns-prefetch" crossorigin="">
<link href="//s.go-mpulse.net" rel="dns-prefetch" crossorigin="">
<link href="//dpm.demdex.net" rel="preconnect">
<link href="//standchartbank.demdex.net" rel="preconnect">
<link href="//standchartbank.tt.omtrdc.net" rel="preconnect">
<link href="//standchartbank.sc.omtrdc.net" rel="preconnect">
<link href="//fast.standchartbank.demdex.net" rel="preconnect">
<meta name="description" content="Borrowing money in Hong Kong with SC Personal Instalment Loan. Receives up to HKD4 million/18x your monthly salary with an interest rate as low as 1.85%."><!-- WP SEO -->
			<meta name="sc:country" content="hk">
	
				<meta name="sc:segment" content="personal">
	
	
			<meta name="sc:categories" content="loan,product">
	
	
			<meta name="sc:page-slug" content="personal-instalment-loan">
	
		<meta name="sc:page-has-no-translation" content="">
	<link rel="stylesheet" id="videojs-css" href="https://av.sc.com/assets/global/css/vendor.min.css?ver=b0b95ac" media="all">
<link rel="stylesheet" id="sc_retail-style-css" href="https://av.sc.com/assets/global/css/style-base.min.css?ver=b0b95ac" media="all">
<link rel="stylesheet" id="sc_retail-style-print-css" href="https://av.sc.com/assets/global/css/style-print.min.css?ver=b0b95ac" media="print">
<link rel="stylesheet" id="sc_retail-style-mobile-css" href="https://av.sc.com/assets/global/css/style-mobile.min.css?ver=b0b95ac" media="(max-width: 767px)">
<link rel="stylesheet" id="sc_retail-style-tablet-css" href="https://av.sc.com/assets/global/css/style-tablet.min.css?ver=b0b95ac" media="(min-width: 768px)">
<link rel="stylesheet" id="sc_retail-style-desktop-css" href="https://av.sc.com/assets/global/css/style-desktop.min.css?ver=b0b95ac" media="(min-width: 1024px)">
<link rel="stylesheet" id="sc-onetrust-cookie-implicit-style-css" href="https://av.sc.com/assets/global/css/onetrust-cookie-custom-implicit.min.css?ver=b0b95ac" media="all">
<script src="https://av.sc.com/assets/global/js/utils.min.js?ver=b0b95ac" id="utility-js"></script>
<script src="https://av.sc.com/assets/global/js/head.min.js?ver=b0b95ac" id="headjs-js"></script>
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
<meta name="title" content="Personal Instalment Loan | Interest rate as low as 1.85% | Hong Kong - Standard Chartered HK">
<link rel="alternate" href="https://www.sc.com/hk/zh/loans/personal-instalment-loan/" hreflang="zh-HK">
<link rel="alternate" href="https://www.sc.com/hk/loans/personal-instalment-loan/" hreflang="en-US">
<meta property="og:title" content="Personal Instalment Loan | Interest rate as low as 1.85% | Hong Kong - Standard Chartered HK">
<meta property="og:description" content="Borrowing money in Hong Kong with SC Personal Instalment Loan. Receives up to HKD4 million/18x your monthly salary with an interest rate as low as 1.85%.">
<meta property="og:url" content="https://www.sc.com/hk/loans/personal-instalment-loan/">
<meta property="og:image" content="https://av.sc.com/hk/content/images/hk-loans-pil-nov24-pintile-400-400-en.jpg">
<meta property="og:image:width" content="400">
<meta property="og:image:height" content="401">
<meta name="twitter:title" content="Personal Instalment Loan | Interest rate as low as 1.85% | Hong Kong - Standard Chartered HK">
<meta name="twitter:description" content="Borrowing money in Hong Kong with SC Personal Instalment Loan. Receives up to HKD4 million/18x your monthly salary with an interest rate as low as 1.85%.">
<meta name="twitter:image" content="https://av.sc.com/hk/content/images/hk-loans-pil-nov24-pintile-400-400-en.jpg">
	<script>
		var baseURL = "https:\/\/av.sc.com\/assets\/global";
	</script>
	<link href="//av.sc.com/assets/global/fonts/sc-sans-web-regular.woff2" rel="preload" as="font" crossorigin="anonymous">
<link href="//av.sc.com/assets/global/fonts/sc-sans-web-light.woff2" rel="preload" as="font" crossorigin="anonymous">
<link href="//av.sc.com/assets/global/fonts/sc-sans-web-bold.woff2" rel="preload" as="font" crossorigin="anonymous">
<link href="//av.sc.com/assets/global/fonts/sc-sans-web-thin.woff2" rel="preload" as="font" crossorigin="anonymous">
<link rel="icon" href="https://av.sc.com/hk/content/images/content/images/cropped-512x512-1-150x150.png" sizes="32x32">
<link rel="icon" href="https://av.sc.com/hk/content/images/content/images/cropped-512x512-1-200x200.png" sizes="192x192">
<link rel="apple-touch-icon" href="https://av.sc.com/hk/content/images/content/images/cropped-512x512-1-200x200.png">
<meta name="msapplication-TileImage" content="https://av.sc.com/hk/content/images/content/images/cropped-512x512-1-300x300.png">
<script src="https://av.sc.com/assets/tpl/onetrust/production/hk/scripttemplates/202302.1.0/otBannerSdk.js" async="" type="text/javascript"></script><script src="https://assets.adobedtm.com/61284d7ff227/d5d3b7b9040a/de2b20c5c19a/RCc45254203edf402c9874570703437380-source.min.js" async=""></script><style type="text/css" id="c2c-family-injected-css">.c2c_box_wrapper{font-family: "SC Sans Web", sans-serif;}</style><style type="text/css" id="c2c-injected-css">.c2c_help_text, .help-text-wrapper {max-width:500px} .c2c_content {max-width:278px} .c2c_box_wrapper.extended .c2c_content, .c2c_box_wrapper.extended .c2c_content .c2c_list {max-width:151px}</style><style id="onetrust-style">#onetrust-banner-sdk{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}#onetrust-banner-sdk .onetrust-vendors-list-handler{cursor:pointer;color:#1f96db;font-size:inherit;font-weight:bold;text-decoration:none;margin-left:5px}#onetrust-banner-sdk .onetrust-vendors-list-handler:hover{color:#1f96db}#onetrust-banner-sdk:focus{outline:2px solid #000;outline-offset:-2px}#onetrust-banner-sdk a:focus{outline:2px solid #000}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{outline-offset:1px}#onetrust-banner-sdk.ot-bnr-w-logo .ot-bnr-logo{height:64px;width:64px}#onetrust-banner-sdk .ot-close-icon,#onetrust-pc-sdk .ot-close-icon,#ot-sync-ntfy .ot-close-icon{background-size:contain;background-repeat:no-repeat;background-position:center;height:12px;width:12px}#onetrust-banner-sdk .powered-by-logo,#onetrust-banner-sdk .ot-pc-footer-logo a,#onetrust-pc-sdk .powered-by-logo,#onetrust-pc-sdk .ot-pc-footer-logo a,#ot-sync-ntfy .powered-by-logo,#ot-sync-ntfy .ot-pc-footer-logo a{background-size:contain;background-repeat:no-repeat;background-position:center;height:25px;width:152px;display:block;text-decoration:none;font-size:0.75em}#onetrust-banner-sdk .powered-by-logo:hover,#onetrust-banner-sdk .ot-pc-footer-logo a:hover,#onetrust-pc-sdk .powered-by-logo:hover,#onetrust-pc-sdk .ot-pc-footer-logo a:hover,#ot-sync-ntfy .powered-by-logo:hover,#ot-sync-ntfy .ot-pc-footer-logo a:hover{color:#565656}#onetrust-banner-sdk h3 *,#onetrust-banner-sdk h4 *,#onetrust-banner-sdk h6 *,#onetrust-banner-sdk button *,#onetrust-banner-sdk a[data-parent-id] *,#onetrust-pc-sdk h3 *,#onetrust-pc-sdk h4 *,#onetrust-pc-sdk h6 *,#onetrust-pc-sdk button *,#onetrust-pc-sdk a[data-parent-id] *,#ot-sync-ntfy h3 *,#ot-sync-ntfy h4 *,#ot-sync-ntfy h6 *,#ot-sync-ntfy button *,#ot-sync-ntfy a[data-parent-id] *{font-size:inherit;font-weight:inherit;color:inherit}#onetrust-banner-sdk .ot-hide,#onetrust-pc-sdk .ot-hide,#ot-sync-ntfy .ot-hide{display:none !important}#onetrust-banner-sdk button.ot-link-btn:hover,#onetrust-pc-sdk button.ot-link-btn:hover,#ot-sync-ntfy button.ot-link-btn:hover{text-decoration:underline;opacity:1}#onetrust-pc-sdk .ot-sdk-row .ot-sdk-column{padding:0}#onetrust-pc-sdk .ot-sdk-container{padding-right:0}#onetrust-pc-sdk .ot-sdk-row{flex-direction:initial;width:100%}#onetrust-pc-sdk [type="checkbox"]:checked,#onetrust-pc-sdk [type="checkbox"]:not(:checked){pointer-events:initial}#onetrust-pc-sdk [type="checkbox"]:disabled+label::before,#onetrust-pc-sdk [type="checkbox"]:disabled+label:after,#onetrust-pc-sdk [type="checkbox"]:disabled+label{pointer-events:none;opacity:0.7}#onetrust-pc-sdk #vendor-list-content{transform:translate3d(0, 0, 0)}#onetrust-pc-sdk li input[type="checkbox"]{z-index:1}#onetrust-pc-sdk li .ot-checkbox label{z-index:2}#onetrust-pc-sdk li .ot-checkbox input[type="checkbox"]{height:auto;width:auto}#onetrust-pc-sdk li .host-title a,#onetrust-pc-sdk li .ot-host-name a,#onetrust-pc-sdk li .accordion-text,#onetrust-pc-sdk li .ot-acc-txt{z-index:2;position:relative}#onetrust-pc-sdk input{margin:3px 0.1ex}#onetrust-pc-sdk .pc-logo,#onetrust-pc-sdk .ot-pc-logo{height:60px;width:180px;background-position:center;background-size:contain;background-repeat:no-repeat;display:inline-flex;justify-content:center;align-items:center}#onetrust-pc-sdk .pc-logo img,#onetrust-pc-sdk .ot-pc-logo img{max-height:100%;max-width:100%}#onetrust-pc-sdk .screen-reader-only,#onetrust-pc-sdk .ot-scrn-rdr,.ot-sdk-cookie-policy .screen-reader-only,.ot-sdk-cookie-policy .ot-scrn-rdr{border:0;clip:rect(0 0 0 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}#onetrust-pc-sdk.ot-fade-in,.onetrust-pc-dark-filter.ot-fade-in,#onetrust-banner-sdk.ot-fade-in{animation-name:onetrust-fade-in;animation-duration:400ms;animation-timing-function:ease-in-out}#onetrust-pc-sdk.ot-hide{display:none !important}.onetrust-pc-dark-filter.ot-hide{display:none !important}#ot-sdk-btn.ot-sdk-show-settings,#ot-sdk-btn.optanon-show-settings{color:#68b631;border:1px solid #68b631;height:auto;white-space:normal;word-wrap:break-word;padding:0.8em 2em;font-size:0.8em;line-height:1.2;cursor:pointer;-moz-transition:0.1s ease;-o-transition:0.1s ease;-webkit-transition:1s ease;transition:0.1s ease}#ot-sdk-btn.ot-sdk-show-settings:hover,#ot-sdk-btn.optanon-show-settings:hover{color:#fff;background-color:#68b631}.onetrust-pc-dark-filter{background:rgba(0,0,0,0.5);z-index:2147483646;width:100%;height:100%;overflow:hidden;position:fixed;top:0;bottom:0;left:0}@keyframes onetrust-fade-in{0%{opacity:0}100%{opacity:1}}.ot-cookie-label{text-decoration:underline}@media only screen and (min-width: 426px) and (max-width: 896px) and (orientation: landscape){#onetrust-pc-sdk p{font-size:0.75em}}#onetrust-banner-sdk .banner-option-input:focus+label{outline:1px solid #000;outline-style:auto}.category-vendors-list-handler+a:focus,.category-vendors-list-handler+a:focus-visible{outline:2px solid #000}#onetrust-pc-sdk .ot-userid-title{margin-top:10px}#onetrust-pc-sdk .ot-userid-title>span,#onetrust-pc-sdk .ot-userid-timestamp>span{font-weight:700}#onetrust-pc-sdk .ot-userid-desc{font-style:italic}#onetrust-pc-sdk .ot-host-desc a{pointer-events:initial}#onetrust-pc-sdk .ot-ven-hdr>p a{position:relative;z-index:2;pointer-events:initial}#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info a,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info a{margin-right:auto}#onetrust-pc-sdk .ot-pc-footer-logo img{width:136px;height:16px}#onetrust-banner-sdk .ot-optout-signal,#onetrust-pc-sdk .ot-optout-signal{border:1px solid #32ae88;border-radius:3px;padding:5px;margin-bottom:10px;background-color:#f9fffa;font-size:0.85rem;line-height:2}#onetrust-banner-sdk .ot-optout-signal .ot-optout-icon,#onetrust-pc-sdk .ot-optout-signal .ot-optout-icon{display:inline;margin-right:5px}#onetrust-banner-sdk .ot-optout-signal svg,#onetrust-pc-sdk .ot-optout-signal svg{height:20px;width:30px;transform:scale(0.5)}#onetrust-banner-sdk .ot-optout-signal svg path,#onetrust-pc-sdk .ot-optout-signal svg path{fill:#32ae88}
#onetrust-banner-sdk,#onetrust-pc-sdk,#ot-sdk-cookie-policy,#ot-sync-ntfy{font-size:16px}#onetrust-banner-sdk *,#onetrust-banner-sdk ::after,#onetrust-banner-sdk ::before,#onetrust-pc-sdk *,#onetrust-pc-sdk ::after,#onetrust-pc-sdk ::before,#ot-sdk-cookie-policy *,#ot-sdk-cookie-policy ::after,#ot-sdk-cookie-policy ::before,#ot-sync-ntfy *,#ot-sync-ntfy ::after,#ot-sync-ntfy ::before{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}#onetrust-banner-sdk div,#onetrust-banner-sdk span,#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-banner-sdk p,#onetrust-banner-sdk img,#onetrust-banner-sdk svg,#onetrust-banner-sdk button,#onetrust-banner-sdk section,#onetrust-banner-sdk a,#onetrust-banner-sdk label,#onetrust-banner-sdk input,#onetrust-banner-sdk ul,#onetrust-banner-sdk li,#onetrust-banner-sdk nav,#onetrust-banner-sdk table,#onetrust-banner-sdk thead,#onetrust-banner-sdk tr,#onetrust-banner-sdk td,#onetrust-banner-sdk tbody,#onetrust-banner-sdk .ot-main-content,#onetrust-banner-sdk .ot-toggle,#onetrust-banner-sdk #ot-content,#onetrust-banner-sdk #ot-pc-content,#onetrust-banner-sdk .checkbox,#onetrust-pc-sdk div,#onetrust-pc-sdk span,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#onetrust-pc-sdk p,#onetrust-pc-sdk img,#onetrust-pc-sdk svg,#onetrust-pc-sdk button,#onetrust-pc-sdk section,#onetrust-pc-sdk a,#onetrust-pc-sdk label,#onetrust-pc-sdk input,#onetrust-pc-sdk ul,#onetrust-pc-sdk li,#onetrust-pc-sdk nav,#onetrust-pc-sdk table,#onetrust-pc-sdk thead,#onetrust-pc-sdk tr,#onetrust-pc-sdk td,#onetrust-pc-sdk tbody,#onetrust-pc-sdk .ot-main-content,#onetrust-pc-sdk .ot-toggle,#onetrust-pc-sdk #ot-content,#onetrust-pc-sdk #ot-pc-content,#onetrust-pc-sdk .checkbox,#ot-sdk-cookie-policy div,#ot-sdk-cookie-policy span,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy p,#ot-sdk-cookie-policy img,#ot-sdk-cookie-policy svg,#ot-sdk-cookie-policy button,#ot-sdk-cookie-policy section,#ot-sdk-cookie-policy a,#ot-sdk-cookie-policy label,#ot-sdk-cookie-policy input,#ot-sdk-cookie-policy ul,#ot-sdk-cookie-policy li,#ot-sdk-cookie-policy nav,#ot-sdk-cookie-policy table,#ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy tr,#ot-sdk-cookie-policy td,#ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy .ot-main-content,#ot-sdk-cookie-policy .ot-toggle,#ot-sdk-cookie-policy #ot-content,#ot-sdk-cookie-policy #ot-pc-content,#ot-sdk-cookie-policy .checkbox,#ot-sync-ntfy div,#ot-sync-ntfy span,#ot-sync-ntfy h1,#ot-sync-ntfy h2,#ot-sync-ntfy h3,#ot-sync-ntfy h4,#ot-sync-ntfy h5,#ot-sync-ntfy h6,#ot-sync-ntfy p,#ot-sync-ntfy img,#ot-sync-ntfy svg,#ot-sync-ntfy button,#ot-sync-ntfy section,#ot-sync-ntfy a,#ot-sync-ntfy label,#ot-sync-ntfy input,#ot-sync-ntfy ul,#ot-sync-ntfy li,#ot-sync-ntfy nav,#ot-sync-ntfy table,#ot-sync-ntfy thead,#ot-sync-ntfy tr,#ot-sync-ntfy td,#ot-sync-ntfy tbody,#ot-sync-ntfy .ot-main-content,#ot-sync-ntfy .ot-toggle,#ot-sync-ntfy #ot-content,#ot-sync-ntfy #ot-pc-content,#ot-sync-ntfy .checkbox{font-family:inherit;font-weight:normal;-webkit-font-smoothing:auto;letter-spacing:normal;line-height:normal;padding:0;margin:0;height:auto;min-height:0;max-height:none;width:auto;min-width:0;max-width:none;border-radius:0;border:none;clear:none;float:none;position:static;bottom:auto;left:auto;right:auto;top:auto;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;white-space:normal;background:none;overflow:visible;vertical-align:baseline;visibility:visible;z-index:auto;box-shadow:none}#onetrust-banner-sdk label:before,#onetrust-banner-sdk label:after,#onetrust-banner-sdk .checkbox:after,#onetrust-banner-sdk .checkbox:before,#onetrust-pc-sdk label:before,#onetrust-pc-sdk label:after,#onetrust-pc-sdk .checkbox:after,#onetrust-pc-sdk .checkbox:before,#ot-sdk-cookie-policy label:before,#ot-sdk-cookie-policy label:after,#ot-sdk-cookie-policy .checkbox:after,#ot-sdk-cookie-policy .checkbox:before,#ot-sync-ntfy label:before,#ot-sync-ntfy label:after,#ot-sync-ntfy .checkbox:after,#ot-sync-ntfy .checkbox:before{content:"";content:none}
#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{position:relative;width:100%;max-width:100%;margin:0 auto;padding:0 20px;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{width:100%;float:left;box-sizing:border-box;padding:0;display:initial}@media (min-width: 400px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:90%;padding:0}}@media (min-width: 550px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:100%}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{margin-left:4%}#onetrust-banner-sdk .ot-sdk-column:first-child,#onetrust-banner-sdk .ot-sdk-columns:first-child,#onetrust-pc-sdk .ot-sdk-column:first-child,#onetrust-pc-sdk .ot-sdk-columns:first-child,#ot-sdk-cookie-policy .ot-sdk-column:first-child,#ot-sdk-cookie-policy .ot-sdk-columns:first-child{margin-left:0}#onetrust-banner-sdk .ot-sdk-two.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-two.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-two.ot-sdk-columns{width:13.3333333333%}#onetrust-banner-sdk .ot-sdk-three.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-three.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-three.ot-sdk-columns{width:22%}#onetrust-banner-sdk .ot-sdk-four.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-four.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-four.ot-sdk-columns{width:30.6666666667%}#onetrust-banner-sdk .ot-sdk-eight.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eight.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eight.ot-sdk-columns{width:65.3333333333%}#onetrust-banner-sdk .ot-sdk-nine.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-nine.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-nine.ot-sdk-columns{width:74%}#onetrust-banner-sdk .ot-sdk-ten.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-ten.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-ten.ot-sdk-columns{width:82.6666666667%}#onetrust-banner-sdk .ot-sdk-eleven.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eleven.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eleven.ot-sdk-columns{width:91.3333333333%}#onetrust-banner-sdk .ot-sdk-twelve.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-twelve.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-twelve.ot-sdk-columns{width:100%;margin-left:0}}#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6{margin-top:0;font-weight:600;font-family:inherit}#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem;line-height:1.2}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem;line-height:1.25}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem;line-height:1.3}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem;line-height:1.35}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem;line-height:1.5}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem;line-height:1.6}@media (min-width: 550px){#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem}}#onetrust-banner-sdk p,#onetrust-pc-sdk p,#ot-sdk-cookie-policy p{margin:0 0 1em 0;font-family:inherit;line-height:normal}#onetrust-banner-sdk a,#onetrust-pc-sdk a,#ot-sdk-cookie-policy a{color:#565656;text-decoration:underline}#onetrust-banner-sdk a:hover,#onetrust-pc-sdk a:hover,#ot-sdk-cookie-policy a:hover{color:#565656;text-decoration:none}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{display:inline-block;height:38px;padding:0 30px;color:#555;text-align:center;font-size:0.9em;font-weight:400;line-height:38px;letter-spacing:0.01em;text-decoration:none;white-space:nowrap;background-color:transparent;border-radius:2px;border:1px solid #bbb;cursor:pointer;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-button:hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus,#onetrust-pc-sdk .ot-sdk-button:hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus,#ot-sdk-cookie-policy .ot-sdk-button:hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus{color:#333;border-color:#888;opacity:0.7}#onetrust-banner-sdk .ot-sdk-button:focus,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:focus,#onetrust-pc-sdk .ot-sdk-button:focus,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:focus,#ot-sdk-cookie-policy .ot-sdk-button:focus,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:focus{outline:2px solid #000}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-banner-sdk button.ot-sdk-button-primary,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-pc-sdk button.ot-sdk-button-primary,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary,#ot-sdk-cookie-policy button.ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary{color:#fff;background-color:#33c3f0;border-color:#33c3f0}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-banner-sdk button.ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-banner-sdk button.ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:focus,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-pc-sdk button.ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-pc-sdk button.ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:focus{color:#fff;background-color:#1eaedb;border-color:#1eaedb}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{height:38px;padding:6px 10px;background-color:#fff;border:1px solid #d1d1d1;border-radius:4px;box-shadow:none;box-sizing:border-box}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{-webkit-appearance:none;-moz-appearance:none;appearance:none}#onetrust-banner-sdk input[type="text"]:focus,#onetrust-pc-sdk input[type="text"]:focus,#ot-sdk-cookie-policy input[type="text"]:focus{border:1px solid #000;outline:0}#onetrust-banner-sdk label,#onetrust-pc-sdk label,#ot-sdk-cookie-policy label{display:block;margin-bottom:0.5rem;font-weight:600}#onetrust-banner-sdk input[type="checkbox"],#onetrust-pc-sdk input[type="checkbox"],#ot-sdk-cookie-policy input[type="checkbox"]{display:inline}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{list-style:circle inside}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{padding-left:0;margin-top:0}#onetrust-banner-sdk ul ul,#onetrust-pc-sdk ul ul,#ot-sdk-cookie-policy ul ul{margin:1.5rem 0 1.5rem 3rem;font-size:90%}#onetrust-banner-sdk li,#onetrust-pc-sdk li,#ot-sdk-cookie-policy li{margin-bottom:1rem}#onetrust-banner-sdk th,#onetrust-banner-sdk td,#onetrust-pc-sdk th,#onetrust-pc-sdk td,#ot-sdk-cookie-policy th,#ot-sdk-cookie-policy td{padding:12px 15px;text-align:left;border-bottom:1px solid #e1e1e1}#onetrust-banner-sdk button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-container:after,#onetrust-banner-sdk .ot-sdk-row:after,#onetrust-pc-sdk .ot-sdk-container:after,#onetrust-pc-sdk .ot-sdk-row:after,#ot-sdk-cookie-policy .ot-sdk-container:after,#ot-sdk-cookie-policy .ot-sdk-row:after{content:"";display:table;clear:both}#onetrust-banner-sdk .ot-sdk-row,#onetrust-pc-sdk .ot-sdk-row,#ot-sdk-cookie-policy .ot-sdk-row{margin:0;max-width:none;display:block}
#onetrust-banner-sdk{box-shadow:0 0 18px rgba(0,0,0,.2)}#onetrust-banner-sdk.otFlat{position:fixed;z-index:2147483645;bottom:0;right:0;left:0;background-color:#fff;max-height:90%;overflow-x:hidden;overflow-y:auto}#onetrust-banner-sdk.otFlat.top{top:0px;bottom:auto}#onetrust-banner-sdk.otRelFont{font-size:1rem}#onetrust-banner-sdk>.ot-sdk-container{overflow:hidden}#onetrust-banner-sdk::-webkit-scrollbar{width:11px}#onetrust-banner-sdk::-webkit-scrollbar-thumb{border-radius:10px;background:#c1c1c1}#onetrust-banner-sdk{scrollbar-arrow-color:#c1c1c1;scrollbar-darkshadow-color:#c1c1c1;scrollbar-face-color:#c1c1c1;scrollbar-shadow-color:#c1c1c1}#onetrust-banner-sdk #onetrust-policy{margin:1.25em 0 .625em 2em;overflow:hidden}#onetrust-banner-sdk #onetrust-policy .ot-gv-list-handler{float:left;font-size:.82em;padding:0;margin-bottom:0;border:0;line-height:normal;height:auto;width:auto}#onetrust-banner-sdk #onetrust-policy-title{font-size:1.2em;line-height:1.3;margin-bottom:10px}#onetrust-banner-sdk #onetrust-policy-text{clear:both;text-align:left;font-size:.88em;line-height:1.4}#onetrust-banner-sdk #onetrust-policy-text *{font-size:inherit;line-height:inherit}#onetrust-banner-sdk #onetrust-policy-text a{font-weight:bold;margin-left:5px}#onetrust-banner-sdk #onetrust-policy-title,#onetrust-banner-sdk #onetrust-policy-text{color:dimgray;float:left}#onetrust-banner-sdk #onetrust-button-group-parent{min-height:1px;text-align:center}#onetrust-banner-sdk #onetrust-button-group{display:inline-block}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{background-color:#68b631;color:#fff;border-color:#68b631;margin-right:1em;min-width:125px;height:auto;white-space:normal;word-break:break-word;word-wrap:break-word;padding:12px 10px;line-height:1.2;font-size:.813em;font-weight:600}#onetrust-banner-sdk #onetrust-pc-btn-handler.cookie-setting-link{background-color:#fff;border:none;color:#68b631;text-decoration:underline;padding-left:0;padding-right:0}#onetrust-banner-sdk .onetrust-close-btn-ui{width:44px;height:44px;background-size:12px;border:none;position:relative;margin:auto;padding:0}#onetrust-banner-sdk .banner_logo{display:none}#onetrust-banner-sdk.ot-bnr-w-logo .ot-bnr-logo{position:absolute;top:50%;transform:translateY(-50%);left:0px}#onetrust-banner-sdk.ot-bnr-w-logo #onetrust-policy{margin-left:65px}#onetrust-banner-sdk .ot-b-addl-desc{clear:both;float:left;display:block}#onetrust-banner-sdk #banner-options{float:left;display:table;margin-right:0;margin-left:1em;width:calc(100% - 1em)}#onetrust-banner-sdk .banner-option-input{cursor:pointer;width:auto;height:auto;border:none;padding:0;padding-right:3px;margin:0 0 10px;font-size:.82em;line-height:1.4}#onetrust-banner-sdk .banner-option-input *{pointer-events:none;font-size:inherit;line-height:inherit}#onetrust-banner-sdk .banner-option-input[aria-expanded=true]~.banner-option-details{display:block;height:auto}#onetrust-banner-sdk .banner-option-input[aria-expanded=true] .ot-arrow-container{transform:rotate(90deg)}#onetrust-banner-sdk .banner-option{margin-bottom:12px;margin-left:0;border:none;float:left;padding:0}#onetrust-banner-sdk .banner-option:first-child{padding-left:2px}#onetrust-banner-sdk .banner-option:not(:first-child){padding:0;border:none}#onetrust-banner-sdk .banner-option-header{cursor:pointer;display:inline-block}#onetrust-banner-sdk .banner-option-header :first-child{color:dimgray;font-weight:bold;float:left}#onetrust-banner-sdk .banner-option-header .ot-arrow-container{display:inline-block;border-top:6px solid transparent;border-bottom:6px solid transparent;border-left:6px solid dimgray;margin-left:10px;vertical-align:middle}#onetrust-banner-sdk .banner-option-details{display:none;font-size:.83em;line-height:1.5;padding:10px 0px 5px 10px;margin-right:10px;height:0px}#onetrust-banner-sdk .banner-option-details *{font-size:inherit;line-height:inherit;color:dimgray}#onetrust-banner-sdk .ot-arrow-container,#onetrust-banner-sdk .banner-option-details{transition:all 300ms ease-in 0s;-webkit-transition:all 300ms ease-in 0s;-moz-transition:all 300ms ease-in 0s;-o-transition:all 300ms ease-in 0s}#onetrust-banner-sdk .ot-dpd-container{float:left}#onetrust-banner-sdk .ot-dpd-title{margin-bottom:10px}#onetrust-banner-sdk .ot-dpd-title,#onetrust-banner-sdk .ot-dpd-desc{font-size:.88em;line-height:1.4;color:dimgray}#onetrust-banner-sdk .ot-dpd-title *,#onetrust-banner-sdk .ot-dpd-desc *{font-size:inherit;line-height:inherit}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-text *{margin-bottom:0}#onetrust-banner-sdk.ot-iab-2 .onetrust-vendors-list-handler{display:block;margin-left:0;margin-top:5px;clear:both;margin-bottom:0;padding:0;border:0;height:auto;width:auto}#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group button{display:block}#onetrust-banner-sdk.ot-close-btn-link{padding-top:25px}#onetrust-banner-sdk.ot-close-btn-link #onetrust-close-btn-container{top:15px;transform:none;right:15px}#onetrust-banner-sdk.ot-close-btn-link #onetrust-close-btn-container button{padding:0;white-space:pre-wrap;border:none;height:auto;line-height:1.5;text-decoration:underline;font-size:.69em}#onetrust-banner-sdk #onetrust-policy-text,#onetrust-banner-sdk .ot-dpd-desc,#onetrust-banner-sdk .ot-b-addl-desc{font-size:.813em;line-height:1.5}#onetrust-banner-sdk .ot-dpd-desc{margin-bottom:10px}#onetrust-banner-sdk .ot-dpd-desc>.ot-b-addl-desc{margin-top:10px;margin-bottom:10px;font-size:1em}@media only screen and (max-width: 425px){#onetrust-banner-sdk #onetrust-close-btn-container{position:absolute;top:6px;right:2px}#onetrust-banner-sdk #onetrust-policy{margin-left:0;margin-top:3em}#onetrust-banner-sdk #onetrust-button-group{display:block}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{width:100%}#onetrust-banner-sdk .onetrust-close-btn-ui{top:auto;transform:none}#onetrust-banner-sdk #onetrust-policy-title{display:inline;float:none}#onetrust-banner-sdk #banner-options{margin:0;padding:0;width:100%}}@media only screen and (min-width: 426px)and (max-width: 896px){#onetrust-banner-sdk #onetrust-close-btn-container{position:absolute;top:0;right:0}#onetrust-banner-sdk #onetrust-policy{margin-left:1em;margin-right:1em}#onetrust-banner-sdk .onetrust-close-btn-ui{top:10px;right:10px}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-group-container{width:95%}#onetrust-banner-sdk.ot-iab-2 #onetrust-group-container{width:100%}#onetrust-banner-sdk.ot-bnr-w-logo #onetrust-button-group-parent{padding-left:50px}#onetrust-banner-sdk #onetrust-button-group-parent{width:100%;position:relative;margin-left:0}#onetrust-banner-sdk #onetrust-button-group button{display:inline-block}#onetrust-banner-sdk #onetrust-button-group{margin-right:0;text-align:center}#onetrust-banner-sdk .has-reject-all-button #onetrust-pc-btn-handler{float:left}#onetrust-banner-sdk .has-reject-all-button #onetrust-reject-all-handler,#onetrust-banner-sdk .has-reject-all-button #onetrust-accept-btn-handler{float:right}#onetrust-banner-sdk .has-reject-all-button #onetrust-button-group{width:calc(100% - 2em);margin-right:0}#onetrust-banner-sdk .has-reject-all-button #onetrust-pc-btn-handler.cookie-setting-link{padding-left:0px;text-align:left}#onetrust-banner-sdk.ot-buttons-fw .ot-sdk-three button{width:100%;text-align:center}#onetrust-banner-sdk.ot-buttons-fw #onetrust-button-group-parent button{float:none}#onetrust-banner-sdk.ot-buttons-fw #onetrust-pc-btn-handler.cookie-setting-link{text-align:center}}@media only screen and (min-width: 550px){#onetrust-banner-sdk .banner-option:not(:first-child){border-left:1px solid #d8d8d8;padding-left:25px}}@media only screen and (min-width: 425px)and (max-width: 550px){#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group,#onetrust-banner-sdk.ot-iab-2 #onetrust-policy,#onetrust-banner-sdk.ot-iab-2 .banner-option{width:100%}}@media only screen and (min-width: 769px){#onetrust-banner-sdk #onetrust-button-group{margin-right:30%}#onetrust-banner-sdk #banner-options{margin-left:2em;margin-right:5em;margin-bottom:1.25em;width:calc(100% - 7em)}}@media only screen and (min-width: 897px)and (max-width: 1023px){#onetrust-banner-sdk.vertical-align-content #onetrust-button-group-parent{position:absolute;top:50%;left:75%;transform:translateY(-50%)}#onetrust-banner-sdk #onetrust-close-btn-container{top:50%;margin:auto;transform:translate(-50%, -50%);position:absolute;padding:0;right:0}#onetrust-banner-sdk #onetrust-close-btn-container button{position:relative;margin:0;right:-22px;top:2px}}@media only screen and (min-width: 1024px){#onetrust-banner-sdk #onetrust-close-btn-container{top:50%;margin:auto;transform:translate(-50%, -50%);position:absolute;right:0}#onetrust-banner-sdk #onetrust-close-btn-container button{right:-12px}#onetrust-banner-sdk #onetrust-policy{margin-left:2em}#onetrust-banner-sdk.vertical-align-content #onetrust-button-group-parent{position:absolute;top:50%;left:60%;transform:translateY(-50%)}#onetrust-banner-sdk .ot-optout-signal{width:50%}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-title{width:50%}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-text,#onetrust-banner-sdk.ot-iab-2 :not(.ot-dpd-desc)>.ot-b-addl-desc{margin-bottom:1em;width:50%;border-right:1px solid #d8d8d8;padding-right:1rem}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-text{margin-bottom:0;padding-bottom:1em}#onetrust-banner-sdk.ot-iab-2 :not(.ot-dpd-desc)>.ot-b-addl-desc{margin-bottom:0;padding-bottom:1em}#onetrust-banner-sdk.ot-iab-2 .ot-dpd-container{width:45%;padding-left:1rem;display:inline-block;float:none}#onetrust-banner-sdk.ot-iab-2 .ot-dpd-title{line-height:1.7}#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group-parent{left:auto;right:4%;margin-left:0}#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group button{display:block}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-button-group-parent{margin:auto;width:30%}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-group-container{width:60%}#onetrust-banner-sdk #onetrust-button-group{margin-right:auto}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{margin-top:1em}}@media only screen and (min-width: 890px){#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group-parent{padding-left:3%;padding-right:4%;margin-left:0}#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group{margin-right:0;margin-top:1.25em;width:100%}#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group button{width:100%;margin-bottom:5px;margin-top:5px}#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group button:last-of-type{margin-bottom:20px}}@media only screen and (min-width: 1280px){#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-group-container{width:55%}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-button-group-parent{width:44%;padding-left:2%;padding-right:2%}#onetrust-banner-sdk:not(.ot-iab-2).vertical-align-content #onetrust-button-group-parent{position:absolute;left:55%}}
        #onetrust-consent-sdk #onetrust-banner-sdk {background-color: #FFFFFF;}
            #onetrust-consent-sdk #onetrust-policy-title,
                    #onetrust-consent-sdk #onetrust-policy-text,
                    #onetrust-consent-sdk .ot-b-addl-desc,
                    #onetrust-consent-sdk .ot-dpd-desc,
                    #onetrust-consent-sdk .ot-dpd-title,
                    #onetrust-consent-sdk #onetrust-policy-text *:not(.onetrust-vendors-list-handler),
                    #onetrust-consent-sdk .ot-dpd-desc *:not(.onetrust-vendors-list-handler),
                    #onetrust-consent-sdk #onetrust-banner-sdk #banner-options *,
                    #onetrust-banner-sdk .ot-cat-header,
                    #onetrust-banner-sdk .ot-optout-signal
                    {
                        color: #696969;
                    }
            #onetrust-consent-sdk #onetrust-banner-sdk .banner-option-details {
                    background-color: #E9E9E9;}
             #onetrust-consent-sdk #onetrust-banner-sdk a[href],
                    #onetrust-consent-sdk #onetrust-banner-sdk a[href] font,
                    #onetrust-consent-sdk #onetrust-banner-sdk .ot-link-btn
                        {
                            color: #3860BE;
                        }#onetrust-consent-sdk #onetrust-accept-btn-handler,
                         #onetrust-banner-sdk #onetrust-reject-all-handler {
                            background-color: #346E4A;border-color: #346E4A;
                color: #FFFFFF;
            }
            #onetrust-consent-sdk #onetrust-banner-sdk *:focus,
            #onetrust-consent-sdk #onetrust-banner-sdk:focus {
               outline-color: #000000;
               outline-width: 1px;
            }
            #onetrust-consent-sdk #onetrust-pc-btn-handler,
            #onetrust-consent-sdk #onetrust-pc-btn-handler.cookie-setting-link {
                color: #346E4A; border-color: #346E4A;
                background-color:
                #FFFFFF;
            }#onetrust-pc-sdk.otPcCenter{overflow:hidden;position:fixed;margin:0 auto;top:5%;right:0;left:0;width:40%;max-width:575px;min-width:575px;border-radius:2.5px;z-index:2147483647;background-color:#fff;-webkit-box-shadow:0px 2px 10px -3px #999;-moz-box-shadow:0px 2px 10px -3px #999;box-shadow:0px 2px 10px -3px #999}#onetrust-pc-sdk.otPcCenter[dir=rtl]{right:0;left:0}#onetrust-pc-sdk.otRelFont{font-size:1rem}#onetrust-pc-sdk .ot-optout-signal{margin-top:.625rem}#onetrust-pc-sdk #ot-addtl-venlst .ot-arw-cntr,#onetrust-pc-sdk #ot-addtl-venlst .ot-plus-minus,#onetrust-pc-sdk .ot-hide-tgl{visibility:hidden}#onetrust-pc-sdk #ot-addtl-venlst .ot-arw-cntr *,#onetrust-pc-sdk #ot-addtl-venlst .ot-plus-minus *,#onetrust-pc-sdk .ot-hide-tgl *{visibility:hidden}#onetrust-pc-sdk #ot-gn-venlst .ot-ven-item .ot-acc-hdr{min-height:40px}#onetrust-pc-sdk .ot-pc-header{height:39px;padding:10px 0 10px 30px;border-bottom:1px solid #e9e9e9}#onetrust-pc-sdk #ot-pc-title,#onetrust-pc-sdk #ot-category-title,#onetrust-pc-sdk .ot-cat-header,#onetrust-pc-sdk #ot-lst-title,#onetrust-pc-sdk .ot-ven-hdr .ot-ven-name,#onetrust-pc-sdk .ot-always-active{font-weight:bold;color:dimgray}#onetrust-pc-sdk .ot-always-active-group .ot-cat-header{width:55%;font-weight:700}#onetrust-pc-sdk .ot-cat-item p{clear:both;float:left;margin-top:10px;margin-bottom:5px;line-height:1.5;font-size:.812em;color:dimgray}#onetrust-pc-sdk .ot-close-icon{height:44px;width:44px;background-size:10px}#onetrust-pc-sdk #ot-pc-title{float:left;font-size:1em;line-height:1.5;margin-bottom:10px;margin-top:10px;width:100%}#onetrust-pc-sdk #accept-recommended-btn-handler{margin-right:10px;margin-bottom:25px;outline-offset:-1px}#onetrust-pc-sdk #ot-pc-desc{clear:both;width:100%;font-size:.812em;line-height:1.5;margin-bottom:25px}#onetrust-pc-sdk #ot-pc-desc a{margin-left:5px}#onetrust-pc-sdk #ot-pc-desc *{font-size:inherit;line-height:inherit}#onetrust-pc-sdk #ot-pc-desc ul li{padding:10px 0px}#onetrust-pc-sdk a{color:#656565;cursor:pointer}#onetrust-pc-sdk a:hover{color:#3860be}#onetrust-pc-sdk label{margin-bottom:0}#onetrust-pc-sdk #vdr-lst-dsc{font-size:.812em;line-height:1.5;padding:10px 15px 5px 15px}#onetrust-pc-sdk button{max-width:394px;padding:12px 30px;line-height:1;word-break:break-word;word-wrap:break-word;white-space:normal;font-weight:bold;height:auto}#onetrust-pc-sdk .ot-link-btn{padding:0;margin-bottom:0;border:0;font-weight:normal;line-height:normal;width:auto;height:auto}#onetrust-pc-sdk #ot-pc-content{position:absolute;overflow-y:scroll;padding-left:0px;padding-right:30px;top:60px;bottom:110px;margin:1px 3px 0 30px;width:calc(100% - 63px)}#onetrust-pc-sdk .ot-vs-list .ot-always-active,#onetrust-pc-sdk .ot-cat-grp .ot-always-active{float:right;clear:none;color:#3860be;margin:0;font-size:.813em;line-height:1.3}#onetrust-pc-sdk .ot-pc-scrollbar::-webkit-scrollbar-track{margin-right:20px}#onetrust-pc-sdk .ot-pc-scrollbar::-webkit-scrollbar{width:11px}#onetrust-pc-sdk .ot-pc-scrollbar::-webkit-scrollbar-thumb{border-radius:10px;background:#d8d8d8}#onetrust-pc-sdk input[type=checkbox]:focus+.ot-acc-hdr{outline:#000 1px solid}#onetrust-pc-sdk .ot-pc-scrollbar{scrollbar-arrow-color:#d8d8d8;scrollbar-darkshadow-color:#d8d8d8;scrollbar-face-color:#d8d8d8;scrollbar-shadow-color:#d8d8d8}#onetrust-pc-sdk .save-preference-btn-handler{margin-right:20px}#onetrust-pc-sdk .ot-pc-refuse-all-handler{margin-right:10px}#onetrust-pc-sdk #ot-pc-desc .privacy-notice-link{margin-left:0;margin-right:8px}#onetrust-pc-sdk #ot-pc-desc .ot-imprint-handler{margin-left:0;margin-right:8px}#onetrust-pc-sdk .ot-subgrp-cntr{display:inline-block;clear:both;width:100%;padding-top:15px}#onetrust-pc-sdk .ot-switch+.ot-subgrp-cntr{padding-top:10px}#onetrust-pc-sdk ul.ot-subgrps{margin:0;font-size:initial}#onetrust-pc-sdk ul.ot-subgrps li p,#onetrust-pc-sdk ul.ot-subgrps li h5{font-size:.813em;line-height:1.4;color:dimgray}#onetrust-pc-sdk ul.ot-subgrps .ot-switch{min-height:auto}#onetrust-pc-sdk ul.ot-subgrps .ot-switch-nob{top:0}#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr{display:inline-block;width:100%}#onetrust-pc-sdk ul.ot-subgrps .ot-acc-txt{margin:0}#onetrust-pc-sdk ul.ot-subgrps li{padding:0;border:none}#onetrust-pc-sdk ul.ot-subgrps li h5{position:relative;top:5px;font-weight:bold;margin-bottom:0;float:left}#onetrust-pc-sdk li.ot-subgrp{margin-left:20px;overflow:auto}#onetrust-pc-sdk li.ot-subgrp>h5{width:calc(100% - 100px)}#onetrust-pc-sdk .ot-cat-item p>ul,#onetrust-pc-sdk li.ot-subgrp p>ul{margin:0px;list-style:disc;margin-left:15px;font-size:inherit}#onetrust-pc-sdk .ot-cat-item p>ul li,#onetrust-pc-sdk li.ot-subgrp p>ul li{font-size:inherit;padding-top:10px;padding-left:0px;padding-right:0px;border:none}#onetrust-pc-sdk .ot-cat-item p>ul li:last-child,#onetrust-pc-sdk li.ot-subgrp p>ul li:last-child{padding-bottom:10px}#onetrust-pc-sdk .ot-pc-logo{height:40px;width:120px}#onetrust-pc-sdk .ot-pc-footer{position:absolute;bottom:0px;width:100%;max-height:160px;border-top:1px solid #d8d8d8}#onetrust-pc-sdk.ot-ftr-stacked .ot-pc-refuse-all-handler{margin-bottom:0px}#onetrust-pc-sdk.ot-ftr-stacked #ot-pc-content{bottom:160px}#onetrust-pc-sdk.ot-ftr-stacked .ot-pc-footer button{width:100%;max-width:none}#onetrust-pc-sdk.ot-ftr-stacked .ot-btn-container{margin:0 30px;width:calc(100% - 60px);padding-right:0}#onetrust-pc-sdk .ot-pc-footer-logo{height:30px;width:100%;text-align:right;background:#f4f4f4}#onetrust-pc-sdk .ot-pc-footer-logo a{display:inline-block;margin-top:5px;margin-right:10px}#onetrust-pc-sdk[dir=rtl] .ot-pc-footer-logo{direction:rtl}#onetrust-pc-sdk[dir=rtl] .ot-pc-footer-logo a{margin-right:25px}#onetrust-pc-sdk .ot-tgl{float:right;position:relative;z-index:1}#onetrust-pc-sdk .ot-tgl input:checked+.ot-switch .ot-switch-nob{background-color:#cddcf2;border:1px solid #3860be}#onetrust-pc-sdk .ot-tgl input:checked+.ot-switch .ot-switch-nob:before{-webkit-transform:translateX(20px);-ms-transform:translateX(20px);transform:translateX(20px);background-color:#3860be;border-color:#3860be}#onetrust-pc-sdk .ot-tgl input:focus+.ot-switch{outline:#000 solid 1px}#onetrust-pc-sdk .ot-switch{position:relative;display:inline-block;width:45px;height:25px}#onetrust-pc-sdk .ot-switch-nob{position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:#f2f1f1;border:1px solid #ddd;transition:all .2s ease-in 0s;-moz-transition:all .2s ease-in 0s;-o-transition:all .2s ease-in 0s;-webkit-transition:all .2s ease-in 0s;border-radius:20px}#onetrust-pc-sdk .ot-switch-nob:before{position:absolute;content:"";height:21px;width:21px;bottom:1px;background-color:#7d7d7d;-webkit-transition:.4s;transition:.4s;border-radius:20px}#onetrust-pc-sdk .ot-chkbox input:checked~label::before{background-color:#3860be}#onetrust-pc-sdk .ot-chkbox input+label::after{content:none;color:#fff}#onetrust-pc-sdk .ot-chkbox input:checked+label::after{content:""}#onetrust-pc-sdk .ot-chkbox input:focus+label::before{outline-style:solid;outline-width:2px;outline-style:auto}#onetrust-pc-sdk .ot-chkbox label{position:relative;display:inline-block;padding-left:30px;cursor:pointer;font-weight:500}#onetrust-pc-sdk .ot-chkbox label::before,#onetrust-pc-sdk .ot-chkbox label::after{position:absolute;content:"";display:inline-block;border-radius:3px}#onetrust-pc-sdk .ot-chkbox label::before{height:18px;width:18px;border:1px solid #3860be;left:0px;top:auto}#onetrust-pc-sdk .ot-chkbox label::after{height:5px;width:9px;border-left:3px solid;border-bottom:3px solid;transform:rotate(-45deg);-o-transform:rotate(-45deg);-ms-transform:rotate(-45deg);-webkit-transform:rotate(-45deg);left:4px;top:5px}#onetrust-pc-sdk .ot-label-txt{display:none}#onetrust-pc-sdk .ot-chkbox input,#onetrust-pc-sdk .ot-tgl input{position:absolute;opacity:0;width:0;height:0}#onetrust-pc-sdk .ot-arw-cntr{float:right;position:relative;pointer-events:none}#onetrust-pc-sdk .ot-arw-cntr .ot-arw{width:16px;height:16px;margin-left:5px;color:dimgray;display:inline-block;vertical-align:middle;-webkit-transition:all 150ms ease-in 0s;-moz-transition:all 150ms ease-in 0s;-o-transition:all 150ms ease-in 0s;transition:all 150ms ease-in 0s}#onetrust-pc-sdk input:checked~.ot-acc-hdr .ot-arw,#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-arw-cntr svg{transform:rotate(90deg);-o-transform:rotate(90deg);-ms-transform:rotate(90deg);-webkit-transform:rotate(90deg)}#onetrust-pc-sdk input[type=checkbox]:focus+.ot-acc-hdr{outline:#000 1px solid}#onetrust-pc-sdk .ot-tgl-cntr,#onetrust-pc-sdk .ot-arw-cntr{display:inline-block}#onetrust-pc-sdk .ot-tgl-cntr{width:45px;float:right;margin-top:2px}#onetrust-pc-sdk #ot-lst-cnt .ot-tgl-cntr{margin-top:10px}#onetrust-pc-sdk .ot-always-active-subgroup{width:auto;padding-left:0px !important;top:3px;position:relative}#onetrust-pc-sdk .ot-label-status{padding-left:5px;font-size:.75em;display:none}#onetrust-pc-sdk .ot-arw-cntr{margin-top:-1px}#onetrust-pc-sdk .ot-arw-cntr svg{-webkit-transition:all 300ms ease-in 0s;-moz-transition:all 300ms ease-in 0s;-o-transition:all 300ms ease-in 0s;transition:all 300ms ease-in 0s;height:10px;width:10px}#onetrust-pc-sdk input:checked~.ot-acc-hdr .ot-arw{transform:rotate(90deg);-o-transform:rotate(90deg);-ms-transform:rotate(90deg);-webkit-transform:rotate(90deg)}#onetrust-pc-sdk .ot-arw{width:10px;margin-left:15px;transition:all 300ms ease-in 0s;-webkit-transition:all 300ms ease-in 0s;-moz-transition:all 300ms ease-in 0s;-o-transition:all 300ms ease-in 0s}#onetrust-pc-sdk .ot-vlst-cntr{margin-bottom:0}#onetrust-pc-sdk .ot-hlst-cntr{margin-top:5px;display:inline-block;width:100%}#onetrust-pc-sdk .category-vendors-list-handler,#onetrust-pc-sdk .category-vendors-list-handler+a,#onetrust-pc-sdk .category-host-list-handler{clear:both;color:#3860be;margin-left:0;font-size:.813em;text-decoration:none;float:left;overflow:hidden}#onetrust-pc-sdk .category-vendors-list-handler:hover,#onetrust-pc-sdk .category-vendors-list-handler+a:hover,#onetrust-pc-sdk .category-host-list-handler:hover{text-decoration-line:underline}#onetrust-pc-sdk .category-vendors-list-handler+a{clear:none}#onetrust-pc-sdk .ot-vlst-cntr .ot-ext-lnk{display:inline-block;height:13px;width:13px;background-repeat:no-repeat;margin-left:1px;margin-top:6px;cursor:pointer}#onetrust-pc-sdk .back-btn-handler{font-size:1em;text-decoration:none}#onetrust-pc-sdk .back-btn-handler:hover{opacity:.6}#onetrust-pc-sdk #ot-lst-title h3{display:inline-block;word-break:break-word;word-wrap:break-word;margin-bottom:0;color:#656565;font-size:1em;font-weight:bold;margin-left:15px}#onetrust-pc-sdk #ot-lst-title{margin:10px 0 10px 0px;font-size:1em;text-align:left}#onetrust-pc-sdk #ot-pc-hdr{margin:0 0 0 30px;height:auto;width:auto}#onetrust-pc-sdk #ot-pc-hdr input::placeholder{color:#d4d4d4;font-style:italic}#onetrust-pc-sdk #vendor-search-handler{height:31px;width:100%;border-radius:50px;font-size:.8em;padding-right:35px;padding-left:15px;float:left;margin-left:15px}#onetrust-pc-sdk .ot-ven-name{display:block;width:auto;padding-right:5px}#onetrust-pc-sdk #ot-lst-cnt{overflow-y:auto;margin-left:20px;margin-right:7px;width:calc(100% - 27px);max-height:calc(100% - 80px);height:100%;transform:translate3d(0, 0, 0)}#onetrust-pc-sdk #ot-pc-lst{width:100%;bottom:100px;position:absolute;top:60px}#onetrust-pc-sdk #ot-pc-lst:not(.ot-enbl-chr) .ot-tgl-cntr .ot-arw-cntr,#onetrust-pc-sdk #ot-pc-lst:not(.ot-enbl-chr) .ot-tgl-cntr .ot-arw-cntr *{visibility:hidden}#onetrust-pc-sdk #ot-pc-lst .ot-tgl-cntr{right:12px;position:absolute}#onetrust-pc-sdk #ot-pc-lst .ot-arw-cntr{float:right;position:relative}#onetrust-pc-sdk #ot-pc-lst .ot-arw{margin-left:10px}#onetrust-pc-sdk #ot-pc-lst .ot-acc-hdr{overflow:hidden;cursor:pointer}#onetrust-pc-sdk .ot-vlst-cntr{overflow:hidden}#onetrust-pc-sdk #ot-sel-blk{overflow:hidden;width:100%;position:sticky;position:-webkit-sticky;top:0;z-index:3}#onetrust-pc-sdk #ot-back-arw{height:12px;width:12px}#onetrust-pc-sdk .ot-lst-subhdr{width:100%;display:inline-block}#onetrust-pc-sdk .ot-search-cntr{float:left;width:78%;position:relative}#onetrust-pc-sdk .ot-search-cntr>svg{width:30px;height:30px;position:absolute;float:left;right:-15px}#onetrust-pc-sdk .ot-fltr-cntr{float:right;right:50px;position:relative}#onetrust-pc-sdk #filter-btn-handler{background-color:#3860be;border-radius:17px;display:inline-block;position:relative;width:32px;height:32px;-moz-transition:.1s ease;-o-transition:.1s ease;-webkit-transition:1s ease;transition:.1s ease;padding:0;margin:0}#onetrust-pc-sdk #filter-btn-handler:hover{background-color:#3860be}#onetrust-pc-sdk #filter-btn-handler svg{width:12px;height:12px;margin:3px 10px 0 10px;display:block;position:static;right:auto;top:auto}#onetrust-pc-sdk .ot-ven-link{color:#3860be;text-decoration:none;font-weight:100;display:inline-block;padding-top:10px;transform:translate(0, 1%);-o-transform:translate(0, 1%);-ms-transform:translate(0, 1%);-webkit-transform:translate(0, 1%);position:relative;z-index:2}#onetrust-pc-sdk .ot-ven-link *{font-size:inherit}#onetrust-pc-sdk .ot-ven-link:hover{text-decoration:underline}#onetrust-pc-sdk .ot-ven-hdr{width:calc(100% - 160px);height:auto;float:left;word-break:break-word;word-wrap:break-word;vertical-align:middle;padding-bottom:3px}#onetrust-pc-sdk .ot-ven-link{letter-spacing:.03em;font-size:.75em;font-weight:400}#onetrust-pc-sdk .ot-ven-dets{border-radius:2px;background-color:#f8f8f8}#onetrust-pc-sdk .ot-ven-dets li:first-child p:first-child{border-top:none}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:not(:first-child){border-top:1px solid #ddd !important}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:nth-child(n+3) p{display:inline-block}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:nth-child(n+3) p:nth-of-type(odd){width:30%}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:nth-child(n+3) p:nth-of-type(even){width:50%;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc p,#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc h4{padding-top:5px;padding-bottom:5px;display:block}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc h4{display:inline-block}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc p:nth-last-child(-n+1){padding-bottom:10px}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc p:nth-child(-n+2):not(.disc-pur){padding-top:10px}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc .disc-pur-cont{display:inline}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc .disc-pur{position:relative;width:50% !important;word-break:break-word;word-wrap:break-word;left:calc(30% + 17px)}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc .disc-pur:nth-child(-n+1){position:static}#onetrust-pc-sdk .ot-ven-dets p,#onetrust-pc-sdk .ot-ven-dets h4,#onetrust-pc-sdk .ot-ven-dets span{font-size:.69em;text-align:left;vertical-align:middle;word-break:break-word;word-wrap:break-word;margin:0;padding-bottom:10px;padding-left:15px;color:#2e3644}#onetrust-pc-sdk .ot-ven-dets h4{padding-top:5px}#onetrust-pc-sdk .ot-ven-dets span{color:dimgray;padding:0;vertical-align:baseline}#onetrust-pc-sdk .ot-ven-dets .ot-ven-pur h4{border-top:1px solid #e9e9e9;border-bottom:1px solid #e9e9e9;padding-bottom:5px;margin-bottom:5px;font-weight:bold}#onetrust-pc-sdk #ot-host-lst .ot-sel-all{float:right;position:relative;margin-right:42px;top:10px}#onetrust-pc-sdk #ot-host-lst .ot-sel-all input[type=checkbox]{width:auto;height:auto}#onetrust-pc-sdk #ot-host-lst .ot-sel-all label{height:20px;width:20px;padding-left:0px}#onetrust-pc-sdk #ot-host-lst .ot-acc-txt{overflow:hidden;width:95%}#onetrust-pc-sdk .ot-host-hdr{position:relative;z-index:1;pointer-events:none;width:calc(100% - 125px);float:left}#onetrust-pc-sdk .ot-host-name,#onetrust-pc-sdk .ot-host-desc{display:inline-block;width:90%}#onetrust-pc-sdk .ot-host-name{pointer-events:none}#onetrust-pc-sdk .ot-host-hdr>a{text-decoration:underline;font-size:.82em;position:relative;z-index:2;float:left;margin-bottom:5px;pointer-events:initial}#onetrust-pc-sdk .ot-host-name+a{margin-top:5px}#onetrust-pc-sdk .ot-host-name,#onetrust-pc-sdk .ot-host-name a,#onetrust-pc-sdk .ot-host-desc,#onetrust-pc-sdk .ot-host-info{color:dimgray;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-host-name,#onetrust-pc-sdk .ot-host-name a{font-weight:bold;font-size:.82em;line-height:1.3}#onetrust-pc-sdk .ot-host-name a{font-size:1em}#onetrust-pc-sdk .ot-host-expand{margin-top:3px;margin-bottom:3px;clear:both;display:block;color:#3860be;font-size:.72em;font-weight:normal}#onetrust-pc-sdk .ot-host-expand *{font-size:inherit}#onetrust-pc-sdk .ot-host-desc,#onetrust-pc-sdk .ot-host-info{font-size:.688em;line-height:1.4;font-weight:normal}#onetrust-pc-sdk .ot-host-desc{margin-top:10px}#onetrust-pc-sdk .ot-host-opt{margin:0;font-size:inherit;display:inline-block;width:100%}#onetrust-pc-sdk .ot-host-opt li>div div{font-size:.8em;padding:5px 0}#onetrust-pc-sdk .ot-host-opt li>div div:nth-child(1){width:30%;float:left}#onetrust-pc-sdk .ot-host-opt li>div div:nth-child(2){width:70%;float:left;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-host-info{border:none;display:inline-block;width:calc(100% - 10px);padding:10px;margin-bottom:10px;background-color:#f8f8f8}#onetrust-pc-sdk .ot-host-info>div{overflow:auto}#onetrust-pc-sdk #no-results{text-align:center;margin-top:30px}#onetrust-pc-sdk #no-results p{font-size:1em;color:#2e3644;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk #no-results p span{font-weight:bold}#onetrust-pc-sdk #ot-fltr-modal{width:100%;height:auto;display:none;-moz-transition:.2s ease;-o-transition:.2s ease;-webkit-transition:2s ease;transition:.2s ease;overflow:hidden;opacity:1;right:0}#onetrust-pc-sdk #ot-fltr-modal .ot-label-txt{display:inline-block;font-size:.85em;color:dimgray}#onetrust-pc-sdk #ot-fltr-cnt{z-index:2147483646;background-color:#fff;position:absolute;height:90%;max-height:300px;width:325px;left:210px;margin-top:10px;margin-bottom:20px;padding-right:10px;border-radius:3px;-webkit-box-shadow:0px 0px 12px 2px #c7c5c7;-moz-box-shadow:0px 0px 12px 2px #c7c5c7;box-shadow:0px 0px 12px 2px #c7c5c7}#onetrust-pc-sdk .ot-fltr-scrlcnt{overflow-y:auto;overflow-x:hidden;clear:both;max-height:calc(100% - 60px)}#onetrust-pc-sdk #ot-anchor{border:12px solid transparent;display:none;position:absolute;z-index:2147483647;right:55px;top:75px;transform:rotate(45deg);-o-transform:rotate(45deg);-ms-transform:rotate(45deg);-webkit-transform:rotate(45deg);background-color:#fff;-webkit-box-shadow:-3px -3px 5px -2px #c7c5c7;-moz-box-shadow:-3px -3px 5px -2px #c7c5c7;box-shadow:-3px -3px 5px -2px #c7c5c7}#onetrust-pc-sdk .ot-fltr-btns{margin-left:15px}#onetrust-pc-sdk #filter-apply-handler{margin-right:15px}#onetrust-pc-sdk .ot-fltr-opt{margin-bottom:25px;margin-left:15px;width:75%;position:relative}#onetrust-pc-sdk .ot-fltr-opt p{display:inline-block;margin:0;font-size:.9em;color:#2e3644}#onetrust-pc-sdk .ot-chkbox label span{font-size:.85em;color:dimgray}#onetrust-pc-sdk .ot-chkbox input[type=checkbox]+label::after{content:none;color:#fff}#onetrust-pc-sdk .ot-chkbox input[type=checkbox]:checked+label::after{content:""}#onetrust-pc-sdk .ot-chkbox input[type=checkbox]:focus+label::before{outline-style:solid;outline-width:2px;outline-style:auto}#onetrust-pc-sdk #ot-selall-vencntr,#onetrust-pc-sdk #ot-selall-adtlvencntr,#onetrust-pc-sdk #ot-selall-hostcntr,#onetrust-pc-sdk #ot-selall-licntr,#onetrust-pc-sdk #ot-selall-gnvencntr{right:15px;position:relative;width:20px;height:20px;float:right}#onetrust-pc-sdk #ot-selall-vencntr label,#onetrust-pc-sdk #ot-selall-adtlvencntr label,#onetrust-pc-sdk #ot-selall-hostcntr label,#onetrust-pc-sdk #ot-selall-licntr label,#onetrust-pc-sdk #ot-selall-gnvencntr label{float:left;padding-left:0}#onetrust-pc-sdk #ot-ven-lst:first-child{border-top:1px solid #e2e2e2}#onetrust-pc-sdk ul{list-style:none;padding:0}#onetrust-pc-sdk ul li{position:relative;margin:0;padding:15px 15px 15px 10px;border-bottom:1px solid #e2e2e2}#onetrust-pc-sdk ul li h3{font-size:.75em;color:#656565;margin:0;display:inline-block;width:70%;height:auto;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk ul li p{margin:0;font-size:.7em}#onetrust-pc-sdk ul li input[type=checkbox]{position:absolute;cursor:pointer;width:100%;height:100%;opacity:0;margin:0;top:0;left:0}#onetrust-pc-sdk .ot-cat-item>button:focus,#onetrust-pc-sdk .ot-acc-cntr>button:focus,#onetrust-pc-sdk li>button:focus{outline:#000 solid 2px}#onetrust-pc-sdk .ot-cat-item>button,#onetrust-pc-sdk .ot-acc-cntr>button,#onetrust-pc-sdk li>button{position:absolute;cursor:pointer;width:100%;height:100%;margin:0;top:0;left:0;z-index:1;max-width:none;border:none}#onetrust-pc-sdk .ot-cat-item>button[aria-expanded=false]~.ot-acc-txt,#onetrust-pc-sdk .ot-acc-cntr>button[aria-expanded=false]~.ot-acc-txt,#onetrust-pc-sdk li>button[aria-expanded=false]~.ot-acc-txt{margin-top:0;max-height:0;opacity:0;overflow:hidden;width:100%;transition:.25s ease-out;display:none}#onetrust-pc-sdk .ot-cat-item>button[aria-expanded=true]~.ot-acc-txt,#onetrust-pc-sdk .ot-acc-cntr>button[aria-expanded=true]~.ot-acc-txt,#onetrust-pc-sdk li>button[aria-expanded=true]~.ot-acc-txt{transition:.1s ease-in;margin-top:10px;width:100%;overflow:auto;display:block}#onetrust-pc-sdk .ot-cat-item>button[aria-expanded=true]~.ot-acc-grpcntr,#onetrust-pc-sdk .ot-acc-cntr>button[aria-expanded=true]~.ot-acc-grpcntr,#onetrust-pc-sdk li>button[aria-expanded=true]~.ot-acc-grpcntr{width:auto;margin-top:0px;padding-bottom:10px}#onetrust-pc-sdk .ot-host-item>button:focus,#onetrust-pc-sdk .ot-ven-item>button:focus{outline:0;border:2px solid #000}#onetrust-pc-sdk .ot-hide-acc>button{pointer-events:none}#onetrust-pc-sdk .ot-hide-acc .ot-plus-minus>*,#onetrust-pc-sdk .ot-hide-acc .ot-arw-cntr>*{visibility:hidden}#onetrust-pc-sdk .ot-hide-acc .ot-acc-hdr{min-height:30px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt){padding-right:10px;width:calc(100% - 37px);margin-top:10px;max-height:calc(100% - 90px)}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk{background-color:#f9f9fc;border:1px solid #e2e2e2;width:calc(100% - 2px);padding-bottom:5px;padding-top:5px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt{border:unset;background-color:unset}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt .ot-sel-all-hdr{display:none}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt .ot-sel-all{padding-right:.5rem}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt .ot-sel-all .ot-chkbox{right:0}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) .ot-sel-all{padding-right:34px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) .ot-sel-all-chkbox{width:auto}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) ul li{border:1px solid #e2e2e2;margin-bottom:10px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) .ot-acc-cntr>.ot-acc-hdr{padding:10px 0 10px 15px}#onetrust-pc-sdk.ot-addtl-vendors .ot-sel-all-chkbox{float:right}#onetrust-pc-sdk.ot-addtl-vendors .ot-plus-minus~.ot-sel-all-chkbox{right:34px}#onetrust-pc-sdk.ot-addtl-vendors #ot-ven-lst:first-child{border-top:none}#onetrust-pc-sdk .ot-acc-cntr{position:relative;border-left:1px solid #e2e2e2;border-right:1px solid #e2e2e2;border-bottom:1px solid #e2e2e2}#onetrust-pc-sdk .ot-acc-cntr input{z-index:1}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr{background-color:#f9f9fc;padding:5px 0 5px 15px;width:auto}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr .ot-plus-minus{vertical-align:middle;top:auto}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr .ot-arw-cntr{right:10px}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr input{z-index:2}#onetrust-pc-sdk .ot-acc-cntr.ot-add-tech .ot-acc-hdr{padding:10px 0 10px 15px}#onetrust-pc-sdk .ot-acc-cntr>input[type=checkbox]:checked~.ot-acc-hdr{border-bottom:1px solid #e2e2e2}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-txt{padding-left:10px;padding-right:10px}#onetrust-pc-sdk .ot-acc-cntr button[aria-expanded=true]~.ot-acc-txt{width:auto}#onetrust-pc-sdk .ot-acc-cntr .ot-addtl-venbox{display:none}#onetrust-pc-sdk .ot-vlst-cntr{margin-bottom:0;width:100%}#onetrust-pc-sdk .ot-vensec-title{font-size:.813em;vertical-align:middle;display:inline-block}#onetrust-pc-sdk .category-vendors-list-handler,#onetrust-pc-sdk .category-vendors-list-handler+a{margin-left:0;margin-top:10px}#onetrust-pc-sdk #ot-selall-vencntr.line-through label::after,#onetrust-pc-sdk #ot-selall-adtlvencntr.line-through label::after,#onetrust-pc-sdk #ot-selall-licntr.line-through label::after,#onetrust-pc-sdk #ot-selall-hostcntr.line-through label::after,#onetrust-pc-sdk #ot-selall-gnvencntr.line-through label::after{height:auto;border-left:0;transform:none;-o-transform:none;-ms-transform:none;-webkit-transform:none;left:5px;top:9px}#onetrust-pc-sdk #ot-category-title{float:left;padding-bottom:10px;font-size:1em;width:100%}#onetrust-pc-sdk .ot-cat-grp{margin-top:10px}#onetrust-pc-sdk .ot-cat-item{line-height:1.1;margin-top:10px;display:inline-block;width:100%}#onetrust-pc-sdk .ot-btn-container{text-align:right}#onetrust-pc-sdk .ot-btn-container button{display:inline-block;font-size:.75em;letter-spacing:.08em;margin-top:19px}#onetrust-pc-sdk #close-pc-btn-handler.ot-close-icon{position:absolute;top:10px;right:0;z-index:1;padding:0;background-color:transparent;border:none}#onetrust-pc-sdk #close-pc-btn-handler.ot-close-icon svg{display:block;height:10px;width:10px}#onetrust-pc-sdk #clear-filters-handler{margin-top:20px;margin-bottom:10px;float:right;max-width:200px;text-decoration:none;color:#3860be;font-size:.9em;font-weight:bold;background-color:transparent;border-color:transparent;padding:1px}#onetrust-pc-sdk #clear-filters-handler:hover{color:#2285f7}#onetrust-pc-sdk #clear-filters-handler:focus{outline:#000 solid 1px}#onetrust-pc-sdk .ot-enbl-chr h4~.ot-tgl,#onetrust-pc-sdk .ot-enbl-chr h4~.ot-always-active{right:45px}#onetrust-pc-sdk .ot-enbl-chr h4~.ot-tgl+.ot-tgl{right:120px}#onetrust-pc-sdk .ot-enbl-chr .ot-pli-hdr.ot-leg-border-color span:first-child{width:90px}#onetrust-pc-sdk .ot-enbl-chr li.ot-subgrp>h5+.ot-tgl-cntr{padding-right:25px}#onetrust-pc-sdk .ot-plus-minus{width:20px;height:20px;font-size:1.5em;position:relative;display:inline-block;margin-right:5px;top:3px}#onetrust-pc-sdk .ot-plus-minus span{position:absolute;background:#27455c;border-radius:1px}#onetrust-pc-sdk .ot-plus-minus span:first-of-type{top:25%;bottom:25%;width:10%;left:45%}#onetrust-pc-sdk .ot-plus-minus span:last-of-type{left:25%;right:25%;height:10%;top:45%}#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-arw,#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-plus-minus span:first-of-type,#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-plus-minus span:last-of-type{transform:rotate(90deg)}#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-plus-minus span:last-of-type{left:50%;right:50%}#onetrust-pc-sdk #ot-selall-vencntr label,#onetrust-pc-sdk #ot-selall-adtlvencntr label,#onetrust-pc-sdk #ot-selall-hostcntr label,#onetrust-pc-sdk #ot-selall-licntr label{position:relative;display:inline-block;width:20px;height:20px}#onetrust-pc-sdk .ot-host-item .ot-plus-minus,#onetrust-pc-sdk .ot-ven-item .ot-plus-minus{float:left;margin-right:8px;top:10px}#onetrust-pc-sdk .ot-ven-item ul{list-style:none inside;font-size:100%;margin:0}#onetrust-pc-sdk .ot-ven-item ul li{margin:0 !important;padding:0;border:none !important}#onetrust-pc-sdk .ot-pli-hdr{color:#77808e;overflow:hidden;padding-top:7.5px;padding-bottom:7.5px;width:calc(100% - 2px);border-top-left-radius:3px;border-top-right-radius:3px}#onetrust-pc-sdk .ot-pli-hdr span:first-child{top:50%;transform:translateY(50%);max-width:90px}#onetrust-pc-sdk .ot-pli-hdr span:last-child{padding-right:10px;max-width:95px;text-align:center}#onetrust-pc-sdk .ot-li-title{float:right;font-size:.813em}#onetrust-pc-sdk .ot-pli-hdr.ot-leg-border-color{background-color:#f4f4f4;border:1px solid #d8d8d8}#onetrust-pc-sdk .ot-pli-hdr.ot-leg-border-color span:first-child{text-align:left;width:70px}#onetrust-pc-sdk li.ot-subgrp>h5,#onetrust-pc-sdk .ot-cat-header{width:calc(100% - 130px)}#onetrust-pc-sdk li.ot-subgrp>h5+.ot-tgl-cntr{padding-left:13px}#onetrust-pc-sdk .ot-acc-grpcntr .ot-acc-grpdesc{margin-bottom:5px}#onetrust-pc-sdk .ot-acc-grpcntr .ot-subgrp-cntr{border-top:1px solid #d8d8d8}#onetrust-pc-sdk .ot-acc-grpcntr .ot-vlst-cntr+.ot-subgrp-cntr{border-top:none}#onetrust-pc-sdk .ot-acc-hdr .ot-arw-cntr+.ot-tgl-cntr,#onetrust-pc-sdk .ot-acc-txt h4+.ot-tgl-cntr{padding-left:13px}#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item .ot-subgrp>h5,#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item .ot-cat-header{width:calc(100% - 145px)}#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item h5+.ot-tgl-cntr,#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item .ot-cat-header+.ot-tgl{padding-left:28px}#onetrust-pc-sdk .ot-sel-all-hdr,#onetrust-pc-sdk .ot-sel-all-chkbox{display:inline-block;width:100%;position:relative}#onetrust-pc-sdk .ot-sel-all-chkbox{z-index:1}#onetrust-pc-sdk .ot-sel-all{margin:0;position:relative;padding-right:23px;float:right}#onetrust-pc-sdk .ot-consent-hdr,#onetrust-pc-sdk .ot-li-hdr{float:right;font-size:.812em;line-height:normal;text-align:center;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-li-hdr{max-width:100px;padding-right:10px}#onetrust-pc-sdk .ot-consent-hdr{max-width:55px}#onetrust-pc-sdk #ot-selall-licntr{display:block;width:21px;height:auto;float:right;position:relative;right:80px}#onetrust-pc-sdk #ot-selall-licntr label{position:absolute}#onetrust-pc-sdk .ot-ven-ctgl{margin-left:66px}#onetrust-pc-sdk .ot-ven-litgl+.ot-arw-cntr{margin-left:81px}#onetrust-pc-sdk .ot-enbl-chr .ot-host-cnt .ot-tgl-cntr{width:auto}#onetrust-pc-sdk #ot-lst-cnt:not(.ot-host-cnt) .ot-tgl-cntr{width:auto;top:auto;height:20px}#onetrust-pc-sdk #ot-lst-cnt .ot-chkbox{position:relative;display:inline-block;width:20px;height:20px}#onetrust-pc-sdk #ot-lst-cnt .ot-chkbox label{position:absolute;padding:0;width:20px;height:20px}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info-cntr{border:1px solid #d8d8d8;padding:.75rem 2rem;padding-bottom:0;width:auto;margin-top:.5rem}#onetrust-pc-sdk .ot-acc-grpdesc+.ot-leg-btn-container{padding-left:20px;padding-right:20px;width:calc(100% - 40px);margin-bottom:5px}#onetrust-pc-sdk .ot-subgrp .ot-leg-btn-container{margin-bottom:5px}#onetrust-pc-sdk #ot-ven-lst .ot-leg-btn-container{margin-top:10px}#onetrust-pc-sdk .ot-leg-btn-container{display:inline-block;width:100%;margin-bottom:10px}#onetrust-pc-sdk .ot-leg-btn-container button{height:auto;padding:6.5px 8px;margin-bottom:0;letter-spacing:0;font-size:.75em;line-height:normal}#onetrust-pc-sdk .ot-leg-btn-container svg{display:none;height:14px;width:14px;padding-right:5px;vertical-align:sub}#onetrust-pc-sdk .ot-active-leg-btn{cursor:default;pointer-events:none}#onetrust-pc-sdk .ot-active-leg-btn svg{display:inline-block}#onetrust-pc-sdk .ot-remove-objection-handler{text-decoration:underline;padding:0;font-size:.75em;font-weight:600;line-height:1;padding-left:10px}#onetrust-pc-sdk .ot-obj-leg-btn-handler span{font-weight:bold;text-align:center;font-size:inherit;line-height:1.5}#onetrust-pc-sdk.ot-close-btn-link #close-pc-btn-handler{border:none;height:auto;line-height:1.5;text-decoration:underline;font-size:.69em;background:none;right:15px;top:15px;width:auto;font-weight:normal}#onetrust-pc-sdk .ot-cat-header{float:left;font-weight:600;font-size:.875em;line-height:1.5;max-width:90%;vertical-align:middle}#onetrust-pc-sdk .ot-vnd-item>button:focus{outline:#000 solid 2px}#onetrust-pc-sdk .ot-vnd-item>button{position:absolute;cursor:pointer;width:100%;height:100%;margin:0;top:0;left:0;z-index:1;max-width:none;border:none}#onetrust-pc-sdk .ot-vnd-item>button[aria-expanded=false]~.ot-acc-txt{margin-top:0;max-height:0;opacity:0;overflow:hidden;width:100%;transition:.25s ease-out;display:none}#onetrust-pc-sdk .ot-vnd-item>button[aria-expanded=true]~.ot-acc-txt{transition:.1s ease-in;margin-top:10px;width:100%;overflow:auto;display:block}#onetrust-pc-sdk .ot-vnd-item>button[aria-expanded=true]~.ot-acc-grpcntr{width:auto;margin-top:0px;padding-bottom:10px}#onetrust-pc-sdk .ot-accordion-layout.ot-cat-item{position:relative;border-radius:2px;margin:0;padding:0;border:1px solid #d8d8d8;border-top:none;width:calc(100% - 2px);float:left}#onetrust-pc-sdk .ot-accordion-layout.ot-cat-item:first-of-type{margin-top:10px;border-top:1px solid #d8d8d8}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpdesc{padding-left:20px;padding-right:20px;width:calc(100% - 40px);font-size:.812em;margin-bottom:10px;margin-top:15px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpdesc>ul{padding-top:10px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpdesc>ul li{padding-top:0;line-height:1.5;padding-bottom:10px}#onetrust-pc-sdk .ot-accordion-layout div+.ot-acc-grpdesc{margin-top:5px}#onetrust-pc-sdk .ot-accordion-layout .ot-vlst-cntr:first-child{margin-top:10px}#onetrust-pc-sdk .ot-accordion-layout .ot-vlst-cntr:last-child,#onetrust-pc-sdk .ot-accordion-layout .ot-hlst-cntr:last-child{margin-bottom:5px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-hdr{padding-top:11.5px;padding-bottom:11.5px;padding-left:20px;padding-right:20px;width:calc(100% - 40px);display:inline-block}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-txt{width:100%;padding:0}#onetrust-pc-sdk .ot-accordion-layout .ot-subgrp-cntr{padding-left:20px;padding-right:15px;padding-bottom:0;width:calc(100% - 35px)}#onetrust-pc-sdk .ot-accordion-layout .ot-subgrp{padding-right:5px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpcntr{z-index:1;position:relative}#onetrust-pc-sdk .ot-accordion-layout .ot-cat-header+.ot-arw-cntr{position:absolute;top:50%;transform:translateY(-50%);right:20px;margin-top:-2px}#onetrust-pc-sdk .ot-accordion-layout .ot-cat-header+.ot-arw-cntr .ot-arw{width:15px;height:20px;margin-left:5px;color:dimgray}#onetrust-pc-sdk .ot-accordion-layout .ot-cat-header{float:none;color:#2e3644;margin:0;display:inline-block;height:auto;word-wrap:break-word;min-height:inherit}#onetrust-pc-sdk .ot-accordion-layout .ot-vlst-cntr,#onetrust-pc-sdk .ot-accordion-layout .ot-hlst-cntr{padding-left:20px;width:calc(100% - 20px);display:inline-block;margin-top:0;padding-bottom:2px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-hdr{position:relative;min-height:25px}#onetrust-pc-sdk .ot-accordion-layout h4~.ot-tgl,#onetrust-pc-sdk .ot-accordion-layout h4~.ot-always-active{position:absolute;top:50%;transform:translateY(-50%);right:20px}#onetrust-pc-sdk .ot-accordion-layout h4~.ot-tgl+.ot-tgl{right:95px}#onetrust-pc-sdk .ot-accordion-layout .category-vendors-list-handler,#onetrust-pc-sdk .ot-accordion-layout .category-vendors-list-handler+a{margin-top:5px}#onetrust-pc-sdk #ot-lst-cnt{margin-top:1rem;max-height:calc(100% - 96px)}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info-cntr{border:1px solid #d8d8d8;padding:.75rem 2rem;padding-bottom:0;width:auto;margin-top:.5rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info{margin-bottom:1rem;padding-left:.75rem;padding-right:.75rem;display:flex;flex-direction:column}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info[data-vnd-info-key*=DPOEmail]{border-top:1px solid #d8d8d8;padding-top:1rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info[data-vnd-info-key*=DPOLink]{border-bottom:1px solid #d8d8d8;padding-bottom:1rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info .ot-vnd-lbl{font-weight:bold;font-size:.85em;margin-bottom:.5rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info .ot-vnd-cnt{margin-left:.5rem;font-weight:500;font-size:.85rem}#onetrust-pc-sdk .ot-vs-list,#onetrust-pc-sdk .ot-vnd-serv{width:auto;padding:1rem 1.25rem;padding-bottom:0}#onetrust-pc-sdk .ot-vs-list .ot-vnd-serv-hdr-cntr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-serv-hdr-cntr{padding-bottom:.75rem;border-bottom:1px solid #d8d8d8}#onetrust-pc-sdk .ot-vs-list .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr{font-weight:600;font-size:.95em;line-height:2;margin-left:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item{border:none;margin:0;padding:0}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item button,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item button{outline:none;border-bottom:1px solid #d8d8d8}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item button[aria-expanded=true],#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item button[aria-expanded=true]{border-bottom:none}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item:first-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item:first-child{margin-top:.25rem;border-top:unset}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item:last-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item:last-child{margin-bottom:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item:last-child button,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item:last-child button{border-bottom:none}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info-cntr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info-cntr{border:1px solid #d8d8d8;padding:.75rem 1.75rem;padding-bottom:0;width:auto;margin-top:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info{margin-bottom:1rem;padding-left:.75rem;padding-right:.75rem;display:flex;flex-direction:column}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOEmail],#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOEmail]{border-top:1px solid #d8d8d8;padding-top:1rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOLink],#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOLink]{border-bottom:1px solid #d8d8d8;padding-bottom:1rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info .ot-vnd-lbl,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info .ot-vnd-lbl{font-weight:bold;font-size:.85em;margin-bottom:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info .ot-vnd-cnt,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info .ot-vnd-cnt{margin-left:.5rem;font-weight:500;font-size:.85rem}#onetrust-pc-sdk .ot-vs-list.ot-vnd-subgrp-cnt,#onetrust-pc-sdk .ot-vnd-serv.ot-vnd-subgrp-cnt{padding-left:40px}#onetrust-pc-sdk .ot-vs-list.ot-vnd-subgrp-cnt .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr,#onetrust-pc-sdk .ot-vnd-serv.ot-vnd-subgrp-cnt .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr{font-size:.8em}#onetrust-pc-sdk .ot-vs-list.ot-vnd-subgrp-cnt .ot-cat-header,#onetrust-pc-sdk .ot-vnd-serv.ot-vnd-subgrp-cnt .ot-cat-header{font-size:.8em}#onetrust-pc-sdk .ot-subgrp-cntr .ot-vnd-serv{margin-bottom:1rem;padding:1rem .95rem}#onetrust-pc-sdk .ot-subgrp-cntr .ot-vnd-serv .ot-vnd-serv-hdr-cntr{padding-bottom:.75rem;border-bottom:1px solid #d8d8d8}#onetrust-pc-sdk .ot-subgrp-cntr .ot-vnd-serv .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr{font-weight:700;font-size:.8em;line-height:20px;margin-left:.82rem}#onetrust-pc-sdk .ot-subgrp-cntr .ot-cat-header{font-weight:700;font-size:.8em;line-height:20px}#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-vnd-serv .ot-vnd-lst-cont .ot-accordion-layout .ot-acc-hdr div.ot-chkbox{margin-left:.82rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr{padding:.5rem 0;margin:0;display:flex;width:100%;align-items:center;justify-content:space-between}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr div:first-child,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr div:first-child,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr div:first-child{margin-left:.5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr div:last-child,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr div:last-child,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr div:last-child{margin-right:.5rem;margin-left:.5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-always-active{position:relative;right:unset;top:unset;transform:unset}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-plus-minus{top:0}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-arw-cntr{float:none;top:unset;right:unset;transform:unset;margin-top:-2px;position:relative}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-cat-header{flex:1;margin:0 .5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-tgl{position:relative;transform:none;right:0;top:0;float:none}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox{position:relative;margin:0 .5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox label{padding:0}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox label::before{position:relative}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox input{position:absolute;cursor:pointer;width:100%;height:100%;opacity:0;margin:0;top:0;left:0;z-index:1}#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps li.ot-subgrp .ot-acc-hdr h5.ot-cat-header,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps li.ot-subgrp .ot-acc-hdr h4.ot-cat-header{margin:0}#onetrust-pc-sdk .ot-vs-config .ot-subgrp-cntr ul.ot-subgrps li.ot-subgrp h5{top:0;line-height:20px}#onetrust-pc-sdk .ot-vs-list{display:flex;flex-direction:column;padding:0;margin:.5rem 4px}#onetrust-pc-sdk .ot-vs-selc-all{display:flex;padding:0;float:unset;align-items:center;justify-content:flex-start}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf{justify-content:flex-end}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf.ot-caret-conf .ot-sel-all-chkbox{margin-right:48px}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf .ot-sel-all-chkbox{margin:0;padding:0;margin-right:14px;justify-content:flex-end}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf #ot-selall-vencntr.ot-chkbox,#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf #ot-selall-vencntr.ot-tgl{display:inline-block;right:unset;width:auto;height:auto;float:none}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf #ot-selall-vencntr label{width:45px;height:25px}#onetrust-pc-sdk .ot-vs-selc-all .ot-sel-all-chkbox{margin-right:11px;margin-left:.75rem;display:flex;align-items:center}#onetrust-pc-sdk .ot-vs-selc-all .sel-all-hdr{margin:0 1.25rem;font-size:.812em;line-height:normal;text-align:center;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-vnd-list-cnt #ot-selall-vencntr.ot-chkbox{float:unset;right:0}#onetrust-pc-sdk[dir=rtl] #ot-back-arw,#onetrust-pc-sdk[dir=rtl] input~.ot-acc-hdr .ot-arw{transform:rotate(180deg);-o-transform:rotate(180deg);-ms-transform:rotate(180deg);-webkit-transform:rotate(180deg)}#onetrust-pc-sdk[dir=rtl] input:checked~.ot-acc-hdr .ot-arw{transform:rotate(270deg);-o-transform:rotate(270deg);-ms-transform:rotate(270deg);-webkit-transform:rotate(270deg)}#onetrust-pc-sdk[dir=rtl] .ot-chkbox label::after{transform:rotate(45deg);-webkit-transform:rotate(45deg);-o-transform:rotate(45deg);-ms-transform:rotate(45deg);border-left:0;border-right:3px solid}#onetrust-pc-sdk[dir=rtl] .ot-search-cntr>svg{right:0}@media only screen and (max-width: 600px){#onetrust-pc-sdk.otPcCenter{left:0;min-width:100%;height:100%;top:0;border-radius:0}#onetrust-pc-sdk #ot-pc-content,#onetrust-pc-sdk.ot-ftr-stacked .ot-btn-container{margin:1px 3px 0 10px;padding-right:10px;width:calc(100% - 23px)}#onetrust-pc-sdk .ot-btn-container button{max-width:none;letter-spacing:.01em}#onetrust-pc-sdk #close-pc-btn-handler{top:10px;right:17px}#onetrust-pc-sdk p{font-size:.7em}#onetrust-pc-sdk #ot-pc-hdr{margin:10px 10px 0 5px;width:calc(100% - 15px)}#onetrust-pc-sdk .vendor-search-handler{font-size:1em}#onetrust-pc-sdk #ot-back-arw{margin-left:12px}#onetrust-pc-sdk #ot-lst-cnt{margin:0;padding:0 5px 0 10px;min-width:95%}#onetrust-pc-sdk .switch+p{max-width:80%}#onetrust-pc-sdk .ot-ftr-stacked button{width:100%}#onetrust-pc-sdk #ot-fltr-cnt{max-width:320px;width:90%;border-top-right-radius:0;border-bottom-right-radius:0;margin:0;margin-left:15px;left:auto;right:40px;top:85px}#onetrust-pc-sdk .ot-fltr-opt{margin-left:25px;margin-bottom:10px}#onetrust-pc-sdk .ot-pc-refuse-all-handler{margin-bottom:0}#onetrust-pc-sdk #ot-fltr-cnt{right:40px}}@media only screen and (max-width: 476px){#onetrust-pc-sdk .ot-fltr-cntr,#onetrust-pc-sdk #ot-fltr-cnt{right:10px}#onetrust-pc-sdk #ot-anchor{right:25px}#onetrust-pc-sdk button{width:100%}#onetrust-pc-sdk:not(.ot-addtl-vendors) #ot-pc-lst:not(.ot-enbl-chr) .ot-sel-all{padding-right:9px}#onetrust-pc-sdk:not(.ot-addtl-vendors) #ot-pc-lst:not(.ot-enbl-chr) .ot-tgl-cntr{right:0}}@media only screen and (max-width: 896px)and (max-height: 425px)and (orientation: landscape){#onetrust-pc-sdk.otPcCenter{left:0;top:0;min-width:100%;height:100%;border-radius:0}#onetrust-pc-sdk #ot-anchor{left:initial;right:50px}#onetrust-pc-sdk #ot-lst-title{margin-top:12px}#onetrust-pc-sdk #ot-lst-title *{font-size:inherit}#onetrust-pc-sdk #ot-pc-hdr input{margin-right:0;padding-right:45px}#onetrust-pc-sdk .switch+p{max-width:85%}#onetrust-pc-sdk #ot-sel-blk{position:static}#onetrust-pc-sdk #ot-pc-lst{overflow:auto}#onetrust-pc-sdk #ot-lst-cnt{max-height:none;overflow:initial}#onetrust-pc-sdk #ot-lst-cnt.no-results{height:auto}#onetrust-pc-sdk input{font-size:1em !important}#onetrust-pc-sdk p{font-size:.6em}#onetrust-pc-sdk #ot-fltr-modal{width:100%;top:0}#onetrust-pc-sdk ul li p,#onetrust-pc-sdk .category-vendors-list-handler,#onetrust-pc-sdk .category-vendors-list-handler+a,#onetrust-pc-sdk .category-host-list-handler{font-size:.6em}#onetrust-pc-sdk.ot-shw-fltr #ot-anchor{display:none !important}#onetrust-pc-sdk.ot-shw-fltr #ot-pc-lst{height:100% !important;overflow:hidden;top:0px}#onetrust-pc-sdk.ot-shw-fltr #ot-fltr-cnt{margin:0;height:100%;max-height:none;padding:10px;top:0;width:calc(100% - 20px);position:absolute;right:0;left:0;max-width:none}#onetrust-pc-sdk.ot-shw-fltr .ot-fltr-scrlcnt{max-height:calc(100% - 65px)}}
            #onetrust-consent-sdk #onetrust-pc-sdk,
                #onetrust-consent-sdk #ot-search-cntr,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-switch.ot-toggle,
                #onetrust-consent-sdk #onetrust-pc-sdk ot-grp-hdr1 .checkbox,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-title:after
                ,#onetrust-consent-sdk #onetrust-pc-sdk #ot-sel-blk,
                        #onetrust-consent-sdk #onetrust-pc-sdk #ot-fltr-cnt,
                        #onetrust-consent-sdk #onetrust-pc-sdk #ot-anchor {
                    background-color: #FFFFFF;
                }
               
            #onetrust-consent-sdk #onetrust-pc-sdk h3,
                #onetrust-consent-sdk #onetrust-pc-sdk h4,
                #onetrust-consent-sdk #onetrust-pc-sdk h5,
                #onetrust-consent-sdk #onetrust-pc-sdk h6,
                #onetrust-consent-sdk #onetrust-pc-sdk p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-ven-lst .ot-ven-opts p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-desc,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-title,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-li-title,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-sel-all-hdr span,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-info,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-fltr-modal #modal-header,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-checkbox label span,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst #ot-sel-blk p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst #ot-lst-title h3,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst .back-btn-handler p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst .ot-ven-name,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst #ot-ven-lst .consent-category,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-inactive-leg-btn,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-label-status,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-chkbox label span,
                #onetrust-consent-sdk #onetrust-pc-sdk #clear-filters-handler,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-optout-signal
                {
                    color: #696969;
                }
             #onetrust-consent-sdk #onetrust-pc-sdk .privacy-notice-link,
                    #onetrust-consent-sdk #onetrust-pc-sdk .category-vendors-list-handler,
                    #onetrust-consent-sdk #onetrust-pc-sdk .category-vendors-list-handler + a,
                    #onetrust-consent-sdk #onetrust-pc-sdk .category-host-list-handler,
                    #onetrust-consent-sdk #onetrust-pc-sdk .ot-ven-link,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-name a,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-acc-hdr .ot-host-expand,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-info a,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-content #ot-pc-desc .ot-link-btn,
                    #onetrust-consent-sdk #onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info a,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info a
                    {
                        color: #3860BE;
                    }
            #onetrust-consent-sdk #onetrust-pc-sdk .category-vendors-list-handler:hover { text-decoration: underline;}
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-acc-grpcntr.ot-acc-txt,
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-acc-txt .ot-subgrp-tgl .ot-switch.ot-toggle
             {
                background-color: #E9E9E9;
            }
             #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-info,
                    #onetrust-consent-sdk #onetrust-pc-sdk .ot-acc-txt .ot-ven-dets
                            {
                                background-color: #E9E9E9;
                            }
        #onetrust-consent-sdk #onetrust-pc-sdk
            button:not(#clear-filters-handler):not(.ot-close-icon):not(#filter-btn-handler):not(.ot-remove-objection-handler):not(.ot-obj-leg-btn-handler):not([aria-expanded]):not(.ot-link-btn),
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-active-leg-btn {
                background-color: #346E4A;border-color: #346E4A;
                color: #FFFFFF;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-active-menu {
                border-color: #346E4A;
            }
            
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-remove-objection-handler{
                background-color: transparent;
                border: 1px solid transparent;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-inactive-leg-btn {
                background-color: #FFFFFF;
                color: #78808E; border-color: #78808E;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-tgl input:focus + .ot-switch, .ot-switch .ot-switch-nob, .ot-switch .ot-switch-nob:before,
            #onetrust-pc-sdk .ot-checkbox input[type="checkbox"]:focus + label::before,
            #onetrust-pc-sdk .ot-chkbox input[type="checkbox"]:focus + label::before {
                outline-color: #000000;
                outline-width: 1px;
            }
            #onetrust-pc-sdk .ot-host-item > button:focus, #onetrust-pc-sdk .ot-ven-item > button:focus {
                border: 1px solid #000000;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk *:focus,
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-vlst-cntr > a:focus {
               outline: 1px solid #000000;
            }#onetrust-pc-sdk .ot-vlst-cntr .ot-ext-lnk {
                    background-image: url('https://av.sc.com/assets/tpl/onetrust/production/hk/consent/dcfcce45-805d-4309-a4b1-704b7638f2c9/301f5d62-0fe6-4311-af94-fbe234a827c4/logos/static/ot_external_link.svg');
                }
            .ot-sdk-cookie-policy{font-family:inherit;font-size:16px}.ot-sdk-cookie-policy.otRelFont{font-size:1rem}.ot-sdk-cookie-policy h3,.ot-sdk-cookie-policy h4,.ot-sdk-cookie-policy h6,.ot-sdk-cookie-policy p,.ot-sdk-cookie-policy li,.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy th,.ot-sdk-cookie-policy #cookie-policy-description,.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}.ot-sdk-cookie-policy h4{font-size:1.2em}.ot-sdk-cookie-policy h6{font-size:1em;margin-top:2em}.ot-sdk-cookie-policy th{min-width:75px}.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy a:hover{background:#fff}.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}.ot-sdk-cookie-policy .ot-mobile-border{display:none}.ot-sdk-cookie-policy section{margin-bottom:2em}.ot-sdk-cookie-policy table{border-collapse:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy{font-family:inherit;font-size:1rem}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup{margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group-desc,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-table-header,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td{font-size:.9em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td a{font-size:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group{font-size:1em;margin-bottom:.6em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-title{margin-bottom:1.2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy>section{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th{min-width:75px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a:hover{background:#fff}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-mobile-border{display:none}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy section{margin-bottom:2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li{list-style:disc;margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li h4{display:inline-block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{border-collapse:inherit;margin:auto;border:1px solid #d7d7d7;border-radius:5px;border-spacing:initial;width:100%;overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border-bottom:1px solid #d7d7d7;border-right:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr th:last-child,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr td:last-child{border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:25%}.ot-sdk-cookie-policy[dir=rtl]{text-align:left}#ot-sdk-cookie-policy h3{font-size:1.5em}@media only screen and (max-width: 530px){.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) table,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tbody,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) th,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{display:block}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead tr{position:absolute;top:-9999px;left:-9999px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{margin:0 0 1em 0}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd),.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd) a{background:#f6f6f4}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td{border:none;border-bottom:1px solid #eee;position:relative;padding-left:50%}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{position:absolute;height:100%;left:6px;width:40%;padding-right:10px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) .ot-mobile-border{display:inline-block;background-color:#e4e4e4;position:absolute;height:100%;top:0;left:45%;width:2px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{content:attr(data-label);font-weight:bold}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border:none;border-bottom:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{display:block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:auto}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{margin:0 0 1em 0}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{height:100%;width:40%;padding-right:10px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{content:attr(data-label);font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead tr{position:absolute;top:-9999px;left:-9999px;z-index:-9999}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:1px solid #d7d7d7;border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td:last-child{border-bottom:0px}}
                
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h5,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group {
                        color: #696969;
                    }
                    
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title {
                            color: #696969;
                        }
                    
            
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th {
                            background-color: #F8F8F8;
                        }
                    
            .ot-floating-button__front{background-image:url('https://av.sc.com/assets/tpl/onetrust/production/hk/consent/dcfcce45-805d-4309-a4b1-704b7638f2c9/301f5d62-0fe6-4311-af94-fbe234a827c4/logos/static/ot_persistent_cookie.png')}
                      @keyframes slide-down-custom {
                          0% {
                              bottom: 720px !important;
                          }
                          100% {
                              bottom: 0px;
                          }
                      }
                      @-webkit-keyframes slide-down-custom {
                          0% {
                              bottom: 720px !important;
                          }
                          100% {
                              bottom: 0px;
                          }
                      }
                      @-moz-keyframes slide-down-custom {
                          0% {
                              bottom: 720px !important;
                          }
                          100% {
                              bottom: 0px;
                          }
                      }
                      #ot-sdk-btn-floating.ot-floating-button{position:fixed;bottom:10px;opacity:0;width:50px;height:50px;line-height:15px;cursor:pointer;background-color:transparent;transition:all 300ms ease;z-index:2147483646;animation:otFloatingBtnIntro 800ms ease 0ms 1 forwards}#ot-sdk-btn-floating.ot-floating-button.ot-hide{display:none}#ot-sdk-btn-floating.ot-floating-button::before,#ot-sdk-btn-floating.ot-floating-button::after{text-transform:none;line-height:1;user-select:none;pointer-events:none;position:absolute;transform:scale(0);opacity:0;transition:all 300ms ease;display:block;height:auto}#ot-sdk-btn-floating.ot-floating-button::before{content:"";border:5px solid transparent;z-index:1001;top:50%;border-left-width:0;border-right-color:#333;right:calc(0em - 5px);transform:translate(10px, -50%)}#ot-sdk-btn-floating.ot-floating-button::after{content:attr(title);position:absolute;text-align:center;top:50%;left:calc(100% + 5px);transform:translate(10px, -50%);font-size:.75rem;min-width:3em;max-width:21em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding:5px;border-radius:.3ch;box-shadow:0 1em 2em -0.5em rgba(0,0,0,.35);background:#333;color:#fff;z-index:2147483645}#ot-sdk-btn-floating.ot-floating-button:hover::before,#ot-sdk-btn-floating.ot-floating-button:hover::after{opacity:1}#ot-sdk-btn-floating.ot-floating-button:hover::before{transform:translate(0.5em, -50%) scale(1)}#ot-sdk-btn-floating.ot-floating-button:hover::after{transform:translate(0.5em, -50%) scale(1)}#ot-sdk-btn-floating.ot-floating-button.ot-pc-open .ot-floating-button__front{transform:rotateY(-180deg)}#ot-sdk-btn-floating.ot-floating-button.ot-pc-open .ot-floating-button__back{transform:rotateY(0)}#ot-sdk-btn-floating .ot-floating-button__front,#ot-sdk-btn-floating .ot-floating-button__back{position:absolute;width:100%;height:100%;-webkit-backface-visibility:hidden;backface-visibility:hidden;background-color:#6aaae4;border-radius:10px;box-shadow:0 4px 8px 0 rgba(0,0,0,.2);transition:transform .6s;transform-style:preserve-3d}#ot-sdk-btn-floating .ot-floating-button__front{background-color:#6aaae4;transform:rotateY(0)}#ot-sdk-btn-floating .ot-floating-button__front.custom-persistent-icon{background-position:center center;background-repeat:no-repeat;background-size:100%;border-radius:100px}#ot-sdk-btn-floating .ot-floating-button__front svg{width:30px;height:37px}#ot-sdk-btn-floating .ot-floating-button__back{background-color:#69c;transform:rotateY(-180deg)}#ot-sdk-btn-floating .ot-floating-button__back.custom-persistent-icon{background-position:center center;background-repeat:no-repeat;background-size:100%;border-radius:100px}#ot-sdk-btn-floating .ot-floating-button__back svg{width:24px;height:24px}#ot-sdk-btn-floating.ot-floating-button button{background-color:transparent;border:0;width:100%;height:100%;cursor:pointer}@keyframes otFloatingBtnIntro{0%{opacity:0;left:-75px}100%{opacity:1;left:1%}}@keyframes otFloatingBtnImageIntro{0%{opacity:0;transform:scale(0) rotate(-270deg)}100%{opacity:100%;transform:scale(0.95) rotate(0deg)}}</style><img width="0" height="0" alt="" src="https://t.teads.tv/track?action=pageView&amp;env=js-web&amp;tag_version=7.2.4_8320d5d&amp;provider=tag&amp;buyer_pixel_id=8962&amp;referer=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F" style="position: absolute;"><script type="text/javascript" async="" src="//t.contentsquare.net/uxa/3bdacf36a16df.js"></script></head>
<body class="page-template-default page page-id-8410 page-parent page-child parent-pageid-7730" data-catch="show-overlay" data-allowed-params="https://av.sc.com/hk/data/whitelist-parameter/allowable/all.json" data-page-ga="1" style="margin-bottom: 80px;"><div class="chatbot-wrapper" style="display:none"><div class="chatbot-window"><div class="chatbot-header-wrapper"><div class="chatbot-header"><div class="close-chat"><span class="c-icon icon-sc-close-chatbot"></span></div><div class="lang-switch" style="display: none;"><a class="active lang" href="#" data-lang="en">EN</a><a class="active lang" href="#" data-lang="zh-HK">中文</a></div><div class="chat-title">Stacy</div><div class="logout-btn" data-lang="en">Log Out</div><div class="logout-btn" data-lang="zh-HK">登出</div></div></div><div class="chatbot-iframe-wrapper"><div class="preloader" style="display: none;"></div><iframe scrolling="yes" title="Chat Widget" frameborder="no" allowfullscreen="" allow="geolocation" class="chatbot-iframe" src="https://av.sc.com/assets/global/chatbot/hk/en/?&amp;title=Stacy&amp;subtitle=Typically%20replies%20instantly&amp;entry-type=HK_UC12_EN&amp;subject-id=HK_BORROW_PERSONAL_INSTALMENT_LOAN_EN&amp;work-group=HK_SALES_CHAT_PAGE"></iframe></div></div></div>

		<!-- Google Tag Manager (noscript) -->
		<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PHQV2K"
		height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
		<!-- End Google Tag Manager (noscript) -->
		<link rel="stylesheet" href="https://av.sc.com/assets/global/css/meganav-rebrand.min.css">
<header class="sc-nav" data-personal-business="true">
    <div class="sc-nav__wrapper">
        <!-- Top Nav -->
        <div class="sc-nav__top">
            <div class="sc-nav__container sc-nav__top-container">
                <div class="sc-nav__top-left">
                    <div class="sc-nav__top-in">
                        <button class="sc-nav__top-btn">Personal</button>
                        <div class="sc-nav__personal-list">
                            <p class="sc-nav__personal-head-mbl only-mobile">Personal</p>
                            <ul class="sc-nav__personal-lists">
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="personal">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/easy-banking/" title="Easy Banking" data-selected-title="personal">
                                        Easy Banking
                                    </a>
                                </li>
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="premium banking">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/premium-banking/" title="Premium Banking" data-selected-title="premium">
                                        Premium Banking
                                    </a>
                                </li>

                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="personal banking">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/priority-banking/" title="Priority Banking" data-selected-title="priority">
                                        Priority Banking
                                    </a>
                                </li>

                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="personal private">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/priority-private/" title="Priority Private" data-selected-title="priority-private">
                                        Priority Private
                                    </a>
                                </li>

                                <!-- 				   <li class="sc-nav__personal-box">
      <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/personal-banking/" title="Easy Banking">
      Easy Banking
      </a>
    </li> -->
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="private banking">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/en/banking/banking-for-individuals/private-banking/" title="Private Banking">
                                        Private Banking
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="sc-nav__top-in">
                        <button class="sc-nav__top-btn">Business</button>
                        <div class="sc-nav__personal-list sc-nav__personal-list-p0">
                            <p class="sc-nav__personal-head-mbl only-mobile">Business</p>
                            <ul class="sc-nav__personal-lists">
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="SME Banking">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/business/" title="SME Banking">
                                        SME Banking
                                    </a>
                                </li>
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="corporate banking">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/en/banking/banking-for-companies/" title="Corporate Banking">
                                        Corporate Banking
                                    </a>
                                </li>
                            </ul>
                            <!--Business S2B Entery points-->
                            <a href="https://s2b.standardchartered.com/unifiedlogin/login/index.html?utm_source=sc.com-hk-en&amp;utm_medium=business-menu-item&amp;utm_campaign=sc-retail-traffic" title="Straight2Bank Login" class="sc-nav__s2bank-lists-box">
                                <div class="sc-nav__s2bank-lists-box-icon">
                                    <span class="sc-nav__s2bank-lists-box-icon__icon">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M15.75 20.25V7.5C15.75 6.67157 16.4216 6 17.25 6C18.0784 6 18.75 6.67157 18.75 7.5V20.25H15.75Z" fill="#38D200"></path>
                                            <path fillrule="evenodd" cliprule="evenodd" d="M10.5 20.25V12C10.5 11.1716 11.1716 10.5 12 10.5C12.8284 10.5 13.5 11.1716 13.5 12V20.25H10.5Z" fill="#0F7AED"></path>
                                            <path d="M8.25 20.25H5.25L5.25 14.625C5.25 13.7966 5.92157 13.125 6.75 13.125C7.57843 13.125 8.25 13.7966 8.25 14.625V20.25Z" fill="#38D200"></path>
                                        </svg>
                                    </span>
                                    Straight2Bank
                                </div>
                                <div class="sc-nav__s2bank-lists-box-desc">
                                    Login to view and manage your business account
                                </div>
                            </a>
                        </div>
                    </div>

                    <div class="sc-nav__top-in">
                        <button class="sc-nav__top-btn">Cross Border</button>
                        <div class="sc-nav__personal-list">
                            <p class="sc-nav__personal-head-mbl only-mobile">Cross Border</p>
                            <ul class="sc-nav__personal-lists">
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="Greater Bay Area Banking">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/gba/" title="Greater Bay Area Banking">
                                        Greater Bay Area Banking
                                    </a>
                                </li>
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="international banking">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/international-banking/" title="International Banking">
                                        International Banking
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="sc-nav__top-in only-mobile">
                        <button class="sc-nav__top-btn">Digital Banking</button>
                        <div class="sc-nav__personal-list sc-nav__personal-list-p0">
                            <p class="sc-nav__personal-head-mbl only-mobile">Digital Banking</p>
                            <ul class="sc-nav__personal-lists">
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="Digital Banking Service Guide ">
                                    <a class="sc-nav__personal-box-link at-element-click-tracking" href="https://www.sc.com/hk/bank-with-us/standard-chartered-digital-banking/" title="Digital Banking Service Guide ">
                                        Digital Banking Service Guide
                                    </a>
                                </li>
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="SC Mobile App download ">
                                    <a class="sc-nav__personal-box-link at-element-click-tracking" href="https://www.sc.com/hk/#sc-lb-module-sc-app-banner" title="SC Mobile App download ">
                                        SC Mobile App download
                                    </a>
                                </li>
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="Payments and Transfers">
                                    <a class="sc-nav__personal-box-link at-element-click-tracking" href="https://www.sc.com/hk/bank-with-us/payments-and-transfers/" title="Payments and Transfers">
                                        Payments and Transfers
                                    </a>
                                </li>
                            </ul>
                            <!--Digital S2B Entery points-->
                            <a href="https://www.sc.com/hk/ibk-redirect/" title="Online Banking" class="sc-nav__s2bank-lists-box">
                                <div class="sc-nav__s2bank-lists-box-icon">
                                    <span class="sc-nav__s2bank-lists-box-icon__icon">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M3.75 15.75H19.875C19.875 17.4069 18.5319 18.75 16.875 18.75H6.75C5.09315 18.75 3.75 17.4069 3.75 15.75Z" fill="#38D200"></path>
                                            <path d="M11.1941 5.25H7.5C6.25736 5.25 5.25 6.25736 5.25 7.5V14.25H18.75V10.3357L17.8036 11.2443C16.9072 12.1049 15.4828 12.0758 14.6223 11.1794C14.1522 10.6897 13.9475 10.0424 14.0048 9.41559L12.375 9.41558C11.1324 9.41558 10.125 8.40822 10.125 7.16558C10.125 6.35604 10.5525 5.64636 11.1941 5.25Z" fill="#0F7AED"></path>
                                            <path fillrule="evenodd" cliprule="evenodd" d="M15.0749 3.7045C15.5142 3.26517 16.2266 3.26517 16.6659 3.7045L20.113 7.15165L19.2238 8.0409L16.6659 10.5988C16.2266 11.0381 15.5142 11.0381 15.0749 10.5988C14.6356 10.1595 14.6356 9.44715 15.0749 9.00781L15.7123 8.3704L12.375 8.3704C11.7537 8.3704 11.25 7.86672 11.25 7.2454C11.25 6.62408 11.7537 6.1204 12.375 6.1204L15.8998 6.1204L15.0749 5.2955C14.6356 4.85616 14.6356 4.14384 15.0749 3.7045Z" fill="#38D200"></path>
                                        </svg>
                                    </span>
                                    Online Banking
                                </div>
                                <div class="sc-nav__s2bank-lists-box-desc">
                                    Login to view account balances &amp; manage transactions
                                </div>
                            </a>
                            <a href="https://s2b.standardchartered.com/unifiedlogin/login/index.html?utm_source=sc.com-hk-en&amp;utm_medium=digital-banking-menu-item&amp;utm_campaign=sc-retail-traffic" title="Straight2Bank Login" class="sc-nav__s2bank-lists-box sc-nav__s2bank-lists-box-2">
                                <div class="sc-nav__s2bank-lists-box-icon">
                                    <span class="sc-nav__s2bank-lists-box-icon__icon">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M15.75 20.25V7.5C15.75 6.67157 16.4216 6 17.25 6C18.0784 6 18.75 6.67157 18.75 7.5V20.25H15.75Z" fill="#38D200"></path>
                                            <path fillrule="evenodd" cliprule="evenodd" d="M10.5 20.25V12C10.5 11.1716 11.1716 10.5 12 10.5C12.8284 10.5 13.5 11.1716 13.5 12V20.25H10.5Z" fill="#0F7AED"></path>
                                            <path d="M8.25 20.25H5.25L5.25 14.625C5.25 13.7966 5.92157 13.125 6.75 13.125C7.57843 13.125 8.25 13.7966 8.25 14.625V20.25Z" fill="#38D200"></path>
                                        </svg>
                                    </span>
                                    Straight2Bank
                                </div>
                                <div class="sc-nav__s2bank-lists-box-desc">
                                    Login to view and manage your business account
                                </div>
                            </a>
                        </div>
                    </div>

                </div>

                <div class="sc-nav__top-right only-desktop">

                    <div class="sc-nav__top-in">
                        <button class="sc-nav__top-btn">Digital Banking</button>
                        <div class="sc-nav__personal-list sc-nav__personal-list-p0">
                            <p class="sc-nav__personal-head-mbl only-mobile">Digital Banking</p>
                            <ul class="sc-nav__personal-lists">
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="Digital Banking Service Guide ">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/bank-with-us/standard-chartered-digital-banking/" title="Digital Banking Service Guide ">
                                        Digital Banking Service Guide
                                    </a>
                                </li>
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="SC Mobile App download ">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/#sc-lb-module-tabs-module-1" title="SC Mobile App download ">
                                        SC Mobile App download
                                    </a>
                                </li>
                                <li class="sc-nav__personal-box">
                                    <meta name="sc:menu-slug" content="Payments and Transfers">
                                    <a class="sc-nav__personal-box-link" href="https://www.sc.com/hk/bank-with-us/payments-and-transfers/" title="Payments and Transfers">
                                        Payments and Transfers
                                    </a>
                                </li>
                            </ul>

                            <!--Digital S2B Entery points-->
                            <a href="https://www.sc.com/hk/ibk-redirect/" title="Online Banking" class="sc-nav__s2bank-lists-box">
                                <div class="sc-nav__s2bank-lists-box-icon">
                                    <span class="sc-nav__s2bank-lists-box-icon__icon">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M3.75 15.75H19.875C19.875 17.4069 18.5319 18.75 16.875 18.75H6.75C5.09315 18.75 3.75 17.4069 3.75 15.75Z" fill="#38D200"></path>
                                            <path d="M11.1941 5.25H7.5C6.25736 5.25 5.25 6.25736 5.25 7.5V14.25H18.75V10.3357L17.8036 11.2443C16.9072 12.1049 15.4828 12.0758 14.6223 11.1794C14.1522 10.6897 13.9475 10.0424 14.0048 9.41559L12.375 9.41558C11.1324 9.41558 10.125 8.40822 10.125 7.16558C10.125 6.35604 10.5525 5.64636 11.1941 5.25Z" fill="#0F7AED"></path>
                                            <path fillrule="evenodd" cliprule="evenodd" d="M15.0749 3.7045C15.5142 3.26517 16.2266 3.26517 16.6659 3.7045L20.113 7.15165L19.2238 8.0409L16.6659 10.5988C16.2266 11.0381 15.5142 11.0381 15.0749 10.5988C14.6356 10.1595 14.6356 9.44715 15.0749 9.00781L15.7123 8.3704L12.375 8.3704C11.7537 8.3704 11.25 7.86672 11.25 7.2454C11.25 6.62408 11.7537 6.1204 12.375 6.1204L15.8998 6.1204L15.0749 5.2955C14.6356 4.85616 14.6356 4.14384 15.0749 3.7045Z" fill="#38D200"></path>
                                        </svg>
                                    </span>
                                    Online Banking
                                </div>
                                <div class="sc-nav__s2bank-lists-box-desc">
                                    Login to view account balances &amp; manage transactions
                                </div>
                            </a>
                            <a href="https://s2b.standardchartered.com/unifiedlogin/login/index.html?utm_source=sc.com-hk-en&amp;utm_medium=digital-banking-menu-item&amp;utm_campaign=sc-retail-traffic" title="Straight2Bank Login" class="sc-nav__s2bank-lists-box sc-nav__s2bank-lists-box-2">
                                <div class="sc-nav__s2bank-lists-box-icon">
                                    <span class="sc-nav__s2bank-lists-box-icon__icon">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M15.75 20.25V7.5C15.75 6.67157 16.4216 6 17.25 6C18.0784 6 18.75 6.67157 18.75 7.5V20.25H15.75Z" fill="#38D200"></path>
                                            <path fillrule="evenodd" cliprule="evenodd" d="M10.5 20.25V12C10.5 11.1716 11.1716 10.5 12 10.5C12.8284 10.5 13.5 11.1716 13.5 12V20.25H10.5Z" fill="#0F7AED"></path>
                                            <path d="M8.25 20.25H5.25L5.25 14.625C5.25 13.7966 5.92157 13.125 6.75 13.125C7.57843 13.125 8.25 13.7966 8.25 14.625V20.25Z" fill="#38D200"></path>
                                        </svg>
                                    </span>
                                    Straight2Bank
                                </div>
                                <div class="sc-nav__s2bank-lists-box-desc">
                                    Login to view and manage your business account
                                </div>
                            </a>
                        </div>
                    </div>
                    <!-- Desktop screen - Services, Help and Search menu -->
                    <ul class="sc-nav__top-menu only-desktop">
                        <!--             <li class="sc-nav__top-item">
    <a href="#" title="Services">
    Services
    </a>
  </li>
  <li class="sc-nav__top-item">
    <a href="#" title="Services">
    Help
    </a>
  </li> -->
                        <li aria-label="Search" class="sc-nav__top-item">
                            <a href="/hk/search/" title="Search" aria-label="Search">
                                <svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M6.34 10.903A4.567 4.567 0 0 1 1.778 6.34 4.568 4.568 0 0 1 6.34 1.777a4.569 4.569 0 0 1 4.564 4.564 4.567 4.567 0 0 1-4.564 4.562m8.73 2.721l-3.596-3.592a6.283 6.283 0 0 0 1.208-3.691A6.348 6.348 0 0 0 6.34 0 6.348 6.348 0 0 0 0 6.34a6.347 6.347 0 0 0 6.34 6.34c1.476 0 2.816-.526 3.895-1.374l3.577 3.575a.887.887 0 0 0 1.257 0 .89.89 0 0 0 0-1.257" fill="#221F20"></path>
                                </svg>
                                <span class="visuallyhidden">Search</span>
                            </a>
                        </li>
                    </ul>

                    <div class="sc-nav__country">
                        <button class="sc-nav__country-btn">
                            Hong Kong
                        </button>
                    </div>
                    <div data-catch="update-language" data-language-sel="en" class="sc-nav__lang c-language-selector">
                        <button class="sc-nav__btn sc-nav__lang-link" data-send="update-language" data-language="zh">
                            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                                <path d="M16.006 0.003c-6.402-0.001-12.188 3.815-14.708 9.7l-0.199 0.066 0.077 0.232c-3.318 8.183 0.626 17.506 8.809 20.823 1.911 0.775 3.954 1.173 6.016 1.172 8.835 0.001 15.998-7.16 15.999-15.994s-7.16-15.998-15.994-15.999zM28.553 24.065l-0.821-0.821v-1.912c0.001-0.083-0.017-0.164-0.053-0.238l-2.080-4.153v-2.007c0-0.178-0.089-0.345-0.237-0.444l-1.6-1.066c-0.125-0.084-0.28-0.11-0.427-0.074l-1.959 0.489-3.291-1.412-0.453-3.172 1.255-1.254h2.693l0.906 1.362c0.082 0.123 0.211 0.206 0.356 0.23l3.199 0.533c0.086 0.014 0.174 0.007 0.256-0.020l2.947-0.982c2.471 4.743 2.207 10.447-0.692 14.941zM26.354 5.258l-0.867 0.578-2.417-0.484-1.568-0.522c-0.096-0.033-0.199-0.037-0.298-0.012l-1.983 0.495-0.869-0.29 0.644-1.288h1.803c0.083 0 0.164-0.019 0.238-0.056l1.845-0.922c1.271 0.663 2.439 1.505 3.471 2.5zM10.161 2.26l1.28 0.853c0.063 0.042 0.134 0.070 0.209 0.082l2.584 0.431-0.252 0.754-1.346 0.45c-0.121 0.040-0.223 0.122-0.288 0.231l-1.531 2.552-2.46 1.476-3.626 0.518c-0.263 0.037-0.458 0.262-0.459 0.527v1.6c0 0.141 0.056 0.277 0.156 0.377l0.91 0.91v0.916l-2.218-1.479-0.805-2.414c1.531-3.498 4.337-6.281 7.847-7.784zM8.642 19.743l-2.41-0.483-0.896-1.787v-1.253l1.987-1.987 0.735 1.471c0.090 0.181 0.275 0.295 0.477 0.295h3.431l1.444 2.407c0.096 0.16 0.27 0.259 0.457 0.259h1.482l-0.373 1.87-2.019 2.019c-0.1 0.1-0.157 0.235-0.157 0.377v1.333l-1.92 1.44c-0.134 0.101-0.213 0.259-0.213 0.427v1.926l-0.663-0.22-0.936-2.342v-5.23c0-0.253-0.178-0.472-0.427-0.523zM7.040 27.94c-5.028-3.772-7.154-10.289-5.318-16.3l0.443 1.329c0.037 0.112 0.111 0.209 0.21 0.275l2.658 1.772-0.606 0.607c-0.1 0.1-0.156 0.236-0.156 0.377v1.6c-0 0.083 0.019 0.164 0.056 0.238l1.066 2.133c0.074 0.147 0.212 0.252 0.373 0.284l2.24 0.447v4.896c-0 0.068 0.013 0.135 0.038 0.198l1.066 2.666c0.058 0.146 0.178 0.258 0.327 0.308l1.6 0.533c0.053 0.018 0.109 0.027 0.166 0.028 0.294 0 0.533-0.239 0.533-0.533v-2.399l1.92-1.44c0.134-0.101 0.213-0.259 0.213-0.427v-1.379l1.977-1.977c0.074-0.074 0.125-0.169 0.146-0.272l0.533-2.666c0.058-0.289-0.13-0.57-0.418-0.627-0.034-0.007-0.069-0.010-0.104-0.010h-1.831l-1.444-2.408c-0.096-0.16-0.27-0.259-0.457-0.259h-3.403l-0.916-1.838c-0.077-0.153-0.223-0.261-0.392-0.288-0.169-0.029-0.342 0.027-0.462 0.149l-0.692 0.689v-0.846c0-0.141-0.056-0.277-0.156-0.377l-0.91-0.91v-0.917l3.275-0.468c0.070-0.010 0.138-0.034 0.199-0.071l2.666-1.6c0.075-0.045 0.137-0.108 0.182-0.182l1.498-2.497 1.412-0.471c0.159-0.052 0.285-0.177 0.337-0.337l0.533-1.6c0.092-0.28-0.059-0.581-0.339-0.674-0.026-0.009-0.052-0.015-0.079-0.020l-3.086-0.515-0.542-0.362c3.356-1.092 6.99-0.957 10.255 0.381l-0.974 0.486h-2.007c-0.203-0.001-0.389 0.113-0.48 0.295l-1.066 2.133c-0.131 0.264-0.024 0.584 0.239 0.715 0.022 0.011 0.046 0.021 0.069 0.029l1.6 0.533c0.096 0.033 0.199 0.037 0.298 0.012l1.983-0.495 1.453 0.484c0.021 0.007 0.042 0.013 0.064 0.017l2.666 0.533c0.139 0.028 0.283-0 0.4-0.079l1.214-0.809c0.597 0.665 1.134 1.382 1.604 2.143l-2.623 0.874-2.84-0.473-0.938-1.408c-0.098-0.147-0.264-0.236-0.441-0.237h-3.199c-0.141 0-0.277 0.056-0.377 0.156l-1.6 1.6c-0.119 0.119-0.175 0.286-0.151 0.453l0.533 3.733c0.027 0.185 0.148 0.342 0.32 0.414l3.733 1.6c0.107 0.046 0.226 0.056 0.339 0.027l1.904-0.476 1.164 0.777v1.848c-0.001 0.083 0.017 0.164 0.053 0.238l2.080 4.153v2.007c0 0.141 0.056 0.277 0.156 0.377l1.116 1.116c-4.947 6.594-14.303 7.929-20.898 2.982z">
                                </path>
                            </svg>

                            中文
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <!-- Menubar -->
        <nav class="sc-nav__nav sc-nav__container">
            <!-- Logo -->
            <div class="sc-nav__logo">
                <a href="https://www.sc.com/hk/" class="sc-nav__logo-link" title="Standard Chartered">
                    <span class="visuallyhidden">Standard Chartered</span>
                </a>
                <a href="https://www.sc.com/hk/" class="sc-nav__logo-drop only-desktop" title="Standard Chartered">
                    <span class="visuallyhidden">Standard Chartered</span>
                </a>
            </div>

            <!-- Menu Section -->
            <ul class="sc-nav__list">
                <!-- Accounts & Deposits -->
                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Banking
                    </button>

                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>

                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-nav-drop__col-wrapper">
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"> <span> Savings
                                                                Accounts</span></div>
                                                        <a title="Marathon Savings Account" class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/marathon-savings-account/">
                                                            Marathon Savings Account
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Wealth Saver Account" class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/wealth-saver/">
                                                            Wealth Saver Account
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Payroll Accounts" class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/payroll-services/">
                                                            Payroll Accounts
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Sustainable Savings Account" class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/savings-accounts/sustainable-savings-account/">
                                                            Sustainable Savings Account
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Integrated Deposit Account" class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/savings-accounts/integrated-deposits-account/">
                                                            Integrated Deposits Account
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>

                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"> <span>Deposit Rates</span>
                                                        </div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/board-rates/" title="Board Rate">Board Rate</a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span>Current
                                                                Accounts</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/current-accounts/hkd-current-account/" title="HKD Current Account">HKD Current Account</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/current-accounts/usd-rmb-current-account/" title="USD &amp; RMB Current Account">USD &amp; RMB Current
                                                            Account</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span><br class="only-desktop-div">Time Deposit</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/online-time-deposit/ " title="Online Time Deposit">Online Time Deposit</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/asia-miles-time-deposit/" title="Asia Miles Time Deposit">Asia Miles Time Deposit</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/foreign-exchange-time-deposit/" title="Foreign Exchange Time Deposit">Foreign Exchange Time
                                                            Deposit</a></div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span>Deposit
                                                                Promotions</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/savings-promotion/" title="Savings">Savings Promotions</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/deposits/time-deposits-promotion/" title="Time Deposit">Time Deposit Promotions</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span><br class="only-desktop-div">Payment / Debit Card</span>
                                                        </div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/bank-with-us/remittance/" title="International Remittance">International
                                                            Remittance</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/bank-with-us/multicurrency-debit-card/" title="Multi-currency Master Debit Card">Multi-currency
                                                            Master Debit Card</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/bank-with-us/atm-card/" title="ATM Card">ATM Card</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                        </div>



                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Marathon Savings Account " href="https://www.sc.com/hk/deposits/marathon-savings-account/">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-deposits-msa-jan25-banner-560-280.jpg" alt="Marathon Savings Account ">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title" style="font-weight:600">
                                                            
                                                            Marathon Savings Account 
                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc" style="height:60px;">
                                                            
                                                            Enjoy up to 4% p.a. in 3 quick steps to grow your wealth.
                                                        
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <!-- View all button -->
                                        <div class="sc-nav-drop__view-all">
                                            <a href="https://www.sc.com/hk/deposits/" class="sc-nav-drop__btn">
                                                View All Banking
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- Credit Cards -->
                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Credit Cards
                    </button>

                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>

                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-nav-drop__col-wrapper">
                                        <div class="sc-nav-drop__col">
                                            <div class="sc-nav-drop__col-label">
                                                <span>Credit Cards</span>
                                            </div>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item" style="min-height: 81px">
                                                    <a title="Cathay Mastercard (Former Asia Miles Mastercard)" href="https://www.sc.com/hk/credit-cards/cathay/"><img class="sc-nav-drop__img" aria-hidden="true" src="https://av.sc.com/hk/content/images/hk-cxam-180x110-2.png" alt="Card Face of Cathay Mastercard" title="Card Face of Cathay Mastercard" style="max-width: 90px;"></a>
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Cathay Mastercard" href="https://www.sc.com/hk/credit-cards/cathay/">
                                                            <p class="sc-nav-drop__link">Cathay Mastercard</p>
                                                            <p class="sc-nav-drop__desc">
                                                                As low as HKD1 = 1 mile
                                                            </p>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item" style="min-height: 81px">
                                                    <a title="Smart Card" href="https://www.sc.com/hk/credit-cards/smart/"><img class="sc-nav-drop__img" aria-hidden="true" src="https://av.sc.com/hk/content/images/hk-sc-cf2-180-110.png" alt="Card Face of Smart Card" title="Card Face of Smart Card" style="max-width: 90px;"></a>
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Smart Card" href="https://www.sc.com/hk/credit-cards/smart/">
                                                            <p class="sc-nav-drop__link">Smart Card</p>
                                                            <p class="sc-nav-drop__desc">
                                                                Up to 5% Cashback
                                                            </p>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item" style="min-height: 81px">
                                                    <a title="Simply Cash Visa Card" href="https://www.sc.com/hk/credit-cards/simplycash/"><img class="sc-nav-drop__img" aria-hidden="true" src="https://av.sc.com/hk/content/images/hk-sccc-180x110-1.png" alt="Card Face of Simply Cash Visa Card" title="Card Face of Simply Cash Visa Card" style="max-width: 90px;"></a>
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Simply Cash Visa Card" href="https://www.sc.com/hk/credit-cards/simplycash/">
                                                            <p class="sc-nav-drop__link">Simply Cash Visa Card</p>
                                                            <p class="sc-nav-drop__desc">
                                                                1.5% Cashback on spending in local currency
                                                            </p>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col">
                                            <span class="sc-nav-drop__col-spacing"></span>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item" style="min-height: 81px">
                                                    <a title="A. Point Card" href="https://www.sc.com/hk/credit-cards/apointcard/"><img class="sc-nav-drop__img" aria-hidden="true" src="https://av.sc.com/hk/content/images/hk-cc-apoint-card-cardface-v2.png" alt="Card Face of A. Point Card" title="Card Face of A. Point Card" style="max-width: 90px;"></a>
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Q Credit Card" href="https://www.sc.com/hk/credit-cards/apointcard/">
                                                            <p class="sc-nav-drop__link">A. Point Card</p>
                                                            <p class="sc-nav-drop__desc">
                                                                Up to 20X A. Point Reward
                                                            </p>
                                                        </a>
                                                    </div>
                                                </li>
                                                <!--<li class="sc-nav-drop__col-item" style="min-height: 81px">
                                                    <a title="Priority Banking Credit Card"
                                                       href="https://www.sc.com/hk/credit-cards/priority-banking/"><img
                                                            class="sc-nav-drop__img" aria-hidden="true"
                                                            src="https://av.sc.com/sg/content/images/sg-priority-visa-infinite-440-280.png"
                                                            alt="Card Face of Priority Banking Credit Card" title="Card Face of Priority Banking Credit Card"/></a>
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Priority Banking Credit Card"
                                                           href="https://www.sc.com/hk/credit-cards/priority-banking/">
                                                            <p class="sc-nav-drop__link">Priority Banking Credit Card</p>
                                                            <p class="sc-nav-drop__desc">
                                                                3x rewards points
                                                            </p>
                                                        </a>
                                                    </div>
                                                </li>-->
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a href="https://www.sc.com/hk/credit-cards/compare/?intcid=pre-web-all-navmenu-1_23-feb-hk-compare_cc_en" title="Credit Card Compare">
                                                            <p class="sc-nav-drop__link">Compare Credit Cards</p>

                                                            <p class="sc-nav-drop__desc">Find The Credit Card Best Fit
                                                                For You</p>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span> Credit Card
                                                                Promotions</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/promotions/the-good-life-year-round-offers/" title="The Good Life Year-round Offers">The Good Life
                                                            Year-round Offers </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/credit-cards/offers/" title="View All Credit Card Promotions →">View All Credit
                                                            Card Promotions → </a></div>
                                                </li>
                                                <li>
                                                    <div class="sc-nav-drop__col-text"></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span><br>Credit Card
                                                                Services</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/credit-cards/new-to-card/" title="New Starter Kit">New Starter Kit</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="360° Rewards Redemption Platform" class="sc-nav-drop__link" href="https://www.sc.com/hk/promotions/credit-cards/new-reward-redemption/">
                                                            360° Rewards
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Credit Card Form And Document Download" class="sc-nav-drop__link" href="https://www.sc.com/hk/help/download-centre/credit-cards-forms-and-documents/">
                                                            Credit Card Form And Document Download
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Credit Card Help Center" class="sc-nav-drop__link" href="https://www.sc.com/hk/help/credit-cards/">
                                                            Credit Card Help Center
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Local Account Fund Transfer by Credit Card" class="sc-nav-drop__link" href="https://www.sc.com/hk/bank-with-us/local-third-party-transfer/#sc-lb-module-product-action-col">
                                                            Local Account Fund Transfer by Credit Card
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Unwarp Double Rewards this Winter" href="https://www.sc.com/hk/credit-cards/cathay/dining/?intcid=nav_cc_t">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-cc-cxam-dining-offer-p3-ot-560-280.jpg" alt="Smart Credit Card">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title" style="font-weight:600">
                                                            Celebrating Flavours with us
                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc" style="height:60px">
                                                            Exclusive dining offers for Standard Chartered Cathay
                                                            Mastercard<sup>®</sup> cardholders. Wine, dine and get
                                                            rewarded now!

                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <!-- View all button -->
                                        <div class="sc-nav-drop__view-all">
                                            <a href="https://www.sc.com/hk/credit-cards/" class="sc-nav-drop__btn">
                                                View All Credit Cards
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- Loans -->

                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Loans
                    </button>

                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>

                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-nav-drop__col-wrapper">
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"> <span> Personal
                                                                Loans</span></div>
                                                        <a title="Personal Instalment Loan" class="sc-nav-drop__link" href="https://www.sc.com/hk/loans/personal-instalment-loan/?intcid=nav_pil_t">
                                                            Personal Instalment Loan
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Personal Instalment Loan Top Up Service" class="sc-nav-drop__link" href="https://www.sc.com/hk/loans/personal-instalment-loan/topup/">
                                                            Personal Instalment Loan Top Up Service
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Debt consolidation programme" class="sc-nav-drop__link" href="https://www.sc.com/hk/loans/debt-consolidation/?intcid=nav_dc_t">
                                                            Debt consolidation programme
                                                        </a>
                                                    </div>
                                                </li>
												<li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Financial Analysis" class="sc-nav-drop__link" href="https://www.sc.com/hk/loans/financial-analysis/">
                                                            Financial Analysis
                                                        </a>
                                                    </div>
                                                </li>
												<li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Electric Vehicle Promotion" class="sc-nav-drop__link" href="https://www.sc.com/hk/loans/personal-instalment-loan/ev-car/">
                                                            Electric Vehicle Promotion
                                                        </a>
                                                        <!--                               <p class="sc-nav-drop__desc">Debt Consolidation</p> -->
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Revolving Cash Card" class="sc-nav-drop__link" href="https://www.sc.com/hk/loans/revolving-cash-card/">
                                                            Revolving Cash Card
                                                        </a>
                                                        <!--                               <p class="sc-nav-drop__desc">Debt Consolidation</p> -->
                                                    </div>
                                                </li>
												<li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Loan Insight &amp; Tips " class="sc-nav-drop__link" href="https://www.sc.com/hk/loans/loan-tips/">
                                                            Loan Insight &amp; Tips 
                                                        </a>
                                                        <!--                               <p class="sc-nav-drop__desc">Debt Consolidation</p> -->
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"> <span>Loans For Existing
                                                                CardHolders</span></div>
                                                        <a title="Get Cash From Credit Card" class="sc-nav-drop__link" href="https://www.sc.com/hk/credit-cards/instalment-credit-program/?intcid=nav_dac_t">
                                                            Get Cash From Credit Card
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Split Your Credit Card Bills" class="sc-nav-drop__link" href="https://www.sc.com/hk/credit-cards/statement-instalment-plan/?intcid=nav_ic2_t">
                                                                Split Your Credit Card Bills
                                                            </a>
                                                        </div>
                                                    </div>
                                                </li>
												<li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Spilt Your Credit Cards Bills (One-off Handling Fee Program)" class="sc-nav-drop__link" href="https://www.sc.com/hk/credit-cards/statement-instalment-plan-fixed-fee/?intcid=nav_ic2_fixedfee_t">
                                                                Spilt Your Credit Cards Bills (One-off Handling Fee Program)
                                                            </a>
                                                        </div>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>


                                        <!-- Promotion -->
                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Bring your dreams to life with daily interest as low as HKD10" href="https://www.sc.com/hk/loans/personal-instalment-loan/?intcid=nav_pil_i">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-loans-pil-summer-campaign-ot-jul24-560-280.jpg" alt="image">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title" style="font-weight:600">
                                                            Bring your dreams to life


                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc" style="height:60px">
                                                            Apply for Personal Instalment Loan to  enjoy daily interest as low as HKD10.
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>

                                        <!-- Promotion -->
                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Spring Specials" href="https://www.sc.com/hk/credit-cards/instalment-credit-program/?intcid=nav_dac_i">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-loans-dac-spring25-624-280-en.jpg" alt="image">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title" style="font-weight:600">
                                                            Spring Specials
                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc" style="height:60px">
                                                            Enjoy up to HKD10,000 CashBack upon successful online application!
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <!-- View all button -->
                                        <div class="sc-nav-drop__view-all">
                                            <a href="https://www.sc.com/hk/loans/" class="sc-nav-drop__btn">
                                                View All Loans
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- Mortgages -->

                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Mortgages
                    </button>

                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>

                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-nav-drop__col-wrapper">
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
												
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
														<div class="sc-nav-drop__col-label"> <span> Mortgage Plans</span></div>
                                                        
                                                        <a title="Deposit Linked Mortgage" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/depositlink/">
                                                            Deposit Linked Mortgage
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Mortgage $aver" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/mortgage-saver/" id="m-aver">
                                                            Mortgage $aver
                                                        </a>
                                                        <!--                               <p class="sc-nav-drop__desc">Debt Consolidation</p> -->
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Up to 90% Mortgage Plan" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/mortgage-insurance-programme/">
                                                            Up to 90% Mortgage Plan
                                                        </a>
                                                        <!--                               <p class="sc-nav-drop__desc">Debt Consolidation</p> -->
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title=" HIBOR Mortgage Plan" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/hibor-based-mortgage/">
                                                            HIBOR Mortgage Plan
                                                        </a>
                                                        <!--                               <p class="sc-nav-drop__desc">Debt Consolidation</p> -->
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span>MORTGAGE TOOLS AND
                                                                FORMS</span></div>
                                                        <a title=" Property Valuation" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/buy-home/search-for-properties/">
                                                            Property Valuation
                                                        </a>
                                                        <!--                               <p class="sc-nav-drop__desc">
          Buy home - Search for properties
          </p> -->
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Mortgage Calculator" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/buy-home/mortgage-assessment-calculators/">
                                                                Mortgage Calculator
                                                            </a>
                                                            <!--                                 <p class="sc-nav-drop__desc">
            Mortgage Planner - Property valuation
          </p> -->
                                                        </div>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Forms &amp; Documents" class="sc-nav-drop__link" href="https://www.sc.com/hk/help/download-centre/mortgage-forms-and-documents/">
                                                                Forms &amp; Documents
                                                            </a>
                                                            <!--                                 <p class="sc-nav-drop__desc">
            Mortgage Planner - Property valuation
          </p> -->
                                                        </div>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"> <span> Mortgage
                                                                Programme</span></div>
                                                        <a title=" Hospital Authority Enhanced HLISS" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/enhanced-home-loan-interest-subsidy-scheme/?intcid=pre-web-all-navmenu-1_23-jan-hk-navmenu_mort_en">
                                                            Hospital Authority Enhanced HLISS
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title=" Green Mortgage" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/green-mortgage-environment-esg/">
                                                                Green Mortgage
                                                            </a>
                                                        </div>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Reverse Mortgage Programme" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/reverse-mortgage-programme/">
                                                                Reverse Mortgage Programme
                                                            </a>
                                                        </div>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Policy Reverse Mortgage Programme" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/policy-reverse-mortgage-programme/">
                                                                Policy Reverse Mortgage Programme
                                                            </a>
                                                            <!--                                 <p class="sc-nav-drop__desc">
            Mortgage Planner - Property valuation
          </p> -->
                                                        </div>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Mortgage Asia Miles Reward" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/mortgage-asia-miles/">
                                                                Mortgage Asia Miles Reward
                                                            </a>
                                                            <!--                                 <p class="sc-nav-drop__desc">
            Mortgage Planner - Property valuation
          </p> -->
                                                        </div>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-text">
                                                            <a title="Greater Bay Area Mortgage" class="sc-nav-drop__link" href="https://www.sc.com/hk/mortgages/home-property-loans/gba-mortgage/">
                                                                Greater Bay Area Mortgage
                                                            </a>

                                                        </div>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <!-- Promotion -->
                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Hospital Authority Enhanced HLISS" href="https://www.sc.com/hk/mortgages/enhanced-home-loan-interest-subsidy-scheme/?intcid=pre-web-all-navmenu-2_23-jan-hk-navmenu_mort_en">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-ha-enhanced-nav-768-350.jpg" alt="image">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title" style="font-weight:600">
                                                            Hospital Authority Enhanced HLISS
                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc">
                                                            Apply now and enjoy a suite of fabulous and exclusive staff
                                                            privileges
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>

                                        <!-- Promotion -->
                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Mortgage Asia Miles Reward" href="https://www.sc.com/hk/mortgages/mortgage-asia-miles/">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-mortgage-asia-miles-reward-768-350.jpg" alt="image">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title" style="font-weight:600">
                                                            Mortgage Asia Miles Reward
                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc">
                                                            Earn 80,000 Asia Miles with HKD4,000,000 mortgage loan
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <!-- View all button -->
                                        <div class="sc-nav-drop__view-all">
                                            <a href="https://www.sc.com/hk/mortgages/" class="sc-nav-drop__btn">
                                                View All Mortgages
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- Investments-->

                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Investment
                    </button>

                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>

                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-nav-drop__col-wrapper">
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"> <span> Wealth
                                                                Solutions</span></div>
                                                        <a title="Investment Fund Services" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/investment-fund-services/">
                                                            Investment Fund Services
                                                        </a>
                                                        <p class="sc-nav-drop__desc" style="font-size: 12px;">Enjoy 0%
                                                            subscription fee for online trades</p>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Securities Services" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/securities-services/">
                                                            Securities Services
                                                        </a>
                                                        <p class="sc-nav-drop__desc" style="font-size: 12px;">Enjoy $0
                                                            trade lodgement fee, custodial fee and account maintenance
                                                            fee</p>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Foreign Exchange" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/foreign-exchange/">
                                                            Foreign Exchange
                                                        </a>
                                                        <p class="sc-nav-drop__desc" style="font-size: 12px;">Welcome
                                                            offer, exclusive exchange rates and cash rewards</p>
                                                    </div>
                                                </li>

                                                <li class="sc-nav-drop__col-item" id="sc-nav-drop__col-item-1">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Online Investment Account" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/online-investment-account/">
                                                            Online Investment Account
                                                        </a>
                                                        <p class="sc-nav-drop__desc" style="font-size: 12px;">A few
                                                            steps to get started</p>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col" id="sc-nav-drop__col_2">
                                            <ul class="sc-nav-drop__col-list">
                                                <!--<li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div">
                                                        <a title="Wealth Lending" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/mywealth/">&nbsp;</a>
                                                    </div>
                                                </li>-->
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="MyWealth Service" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/mywealth/">
                                                            MyWealth Service
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Wealth Lending" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/wealth-lending/">
                                                            Wealth Lending
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Debt Securities Services" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/debt-securities-services/">
                                                            Debt Securities Services
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Equity Linked Investment Services" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/equity-linked-investments/">
                                                            Equity Linked Investment Services (New)
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">

                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"> <span>Investment
                                                                Literacy</span></div>
                                                        <a title="SC Wealth Select" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/sc-wealth-select/">
                                                            SC Wealth Select
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Professional Investors" class="sc-nav-drop__link" href="https://www.sc.com/hk/promotions/professional-investor/">
                                                            Professional Investors
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">

                                                        <a title="Customer Investment Profile" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/customer-investment-profile/">
                                                            Customer Investment Profile
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Use of deposit-related information " class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/investment-financial-services/">
                                                            Use of deposit-related information
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Capital Investment Entrant Scheme" class="sc-nav-drop__link" href="https://www.sc.com/hk/international-banking/new-capital-investment-entrant-scheme/">
                                                            Capital Investment Entrant Scheme
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="sc-nav-drop__col" id="sc-nav-drop__col_3">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label" style="margin-bottom:10px">
                                                            <span>Exclusive Offers</span></div>
                                                        <a title="New or Existing Investment clients" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/investment-client-offers/">
                                                            New or Existing Investment clients
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div" style="height:5px"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label" style="margin-bottom:10px">
                                                            <span>New Launch</span></div>
                                                        <a title="Money Market Funds - 0% Subscription Fee " class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/money-market-funds/">
                                                            Money Market Funds - 0% Subscription Fee
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="Exclusive Digital Offer" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/funds/">
                                                            Fund Explorer

                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div" style="height:5px"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label" style="margin-bottom:10px">
                                                            <span>Insights</span></div>
                                                        <a title="Wealth Guru" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/wealth-guru">
                                                            Wealth Guru
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="FX Market Hub" class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/wealth-guru/fx-market/">
                                                            FX Market Hub
                                                        </a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a title="CIO View" class="sc-nav-drop__link" href="https://www.sc.com/hk/market-outlook/?intcid=web&amp;lang=en&amp;ctry=HK&amp;seg=GWM&amp;channel=PLRB">
                                                            CIO View
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>



                                        <!-- Promotion -->
                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Exclusive privileges for new investment clients" href="https://www.sc.com/hk/investment/signature-cio-funds/#sc-lb-module-video-4">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-wm-signature-cio-2years-ot-400-225-en.jpg" alt="image">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title">
                                                            Signature CIO Funds
                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc">
                                                            Foundational portfolios to navigate safely through market
                                                            uncertainty
                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <!-- View all button -->
                                        <div class="sc-nav-drop__view-all">
                                            <a href="https://www.sc.com/hk/investment/" class="sc-nav-drop__btn">
                                                View All SC Wealth Investments
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- Insure -->
                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Insurance &amp; MPF
                    </button>

                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>

                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-nav-drop__col-wrapper">
                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span>Savings, Retirement
                                                                Planning &amp; MPF</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/life-insurance/savings-legacy-planning/" title="Savings &amp; Protection">Savings &amp; Protection</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/retirement-planning/" title="Retirement Planning">Retirement Planning</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/mpf/" title="MPF Services">MPF</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span><br class="only-desktop-div">Life Protection &amp; Legacy
                                                                Planning</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/life-insurance/wealth-accumulation-legacy-planning/" title="Wealth Accumulation &amp; Legacy Planning">Wealth
                                                            Accumulation &amp; Legacy Planning</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/life-insurance/term-insurance/" title="Term Insurance">Term Insurance</a></div>
                                                </li>
                                            </ul>
                                        </div>

                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span>Medical &amp;
                                                                Accident</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/life-insurance/critical-illness-insurance/" title="Critical Illness Insurance">Critical Illness
                                                            Insurance</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/life-insurance/medical-insurance/" title="Medical Care">Medical Care</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/personal-accident/" title="Personal Accident">Personal Accident</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span><br class="only-desktop-div">Travel, Motor &amp; Home</span>
                                                        </div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/general-insurance/travel-insurance/" title="Travel">Travel</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/motor-insurance/" title="Motor">Motor</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/insurance/household-protection/" title="Household Protection">Household Protection</a></div>
                                                </li>
                                            </ul>
                                        </div>


                                        <div class="sc-nav-drop__col">
                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span>Education</span></div>
                                                        <a class="sc-nav-drop__link" href="https://sc.com/hk/insurance/general-insurance/msig-oversea-study-insurance/" title="Overseas Study Insurance">Overseas Study
                                                            Insurance</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item only-desktop-li">
                                                    <div class="sc-nav-drop__col-text only-desktop-div"><a class="sc-nav-drop__link" href="#" title="">&nbsp;</a></div>
                                                </li>
                                            </ul>


                                            <ul class="sc-nav-drop__col-list">
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text">
                                                        <div class="sc-nav-drop__col-label"><span><br class="only-desktop-div">Useful Tools and
                                                                Resources</span></div>
                                                        <a class="sc-nav-drop__link" href="https://www.sc.com/hk/tools/education-calculator/" title="Education Fund Calculator">Education Fund
                                                            Calculator</a>
                                                    </div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/tax-tactics/" title="Tax Tactics">Tax Tactics</a></div>
                                                </li>
                                                <li class="sc-nav-drop__col-item">
                                                    <div class="sc-nav-drop__col-text"><a class="sc-nav-drop__link" href="https://www.sc.com/hk/investment/wealth-lending/premium-financing/" title="Premium Financing">Premium Financing</a></div>
                                                </li>
                                            </ul>
                                        </div>

                                        <!-- Promotion -->

                                        <div class="sc-nav-drop__col sc-nav-drop__col-promo">
                                            <a title="Allianz Home Protect​" href="https://www.sc.com/hk/insurance/general-insurance/home-insurance/">
                                                <div class="sc-nav-drop__promo-box">
                                                    <img src="https://av.sc.com/hk/content/images/hk-insurance-homeprotect-ot-560-280.png" alt="image">
                                                    <div class="sc-nav-drop__promo-text">
                                                        <p class="sc-nav-drop__promo-title" style="font-weight:600">
                                                            Allianz Home Protect​
                                                        </p>
                                                        <p class="sc-nav-drop__promo-desc" style="height:60px">
                                                            Up to HK$1,500,000 Home Contents protection against fire, theft, typhoon and water damages, etc.

                                                        </p>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>

                                        <!-- View all button -->
                                        <div class="sc-nav-drop__view-all">
                                            <a href="https://www.sc.com/hk/insurance/" class="sc-nav-drop__btn">
                                                View All Insurance
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- Services -->
                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Services
                    </button>
                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>
                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-mgdrop">
                                        <!-- Services meganav Left side contents -->
                                        <div class="sc-mgdrop__left">
                                            <span class="sc-mgdrop__title">Take control of your accounts &amp;
                                                finances</span>
                                            <ul class="sc-mgdrop__list">
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Online Banking" href="https://www.sc.com/hk/bank-with-us/standard-chartered-online-banking/">
                                                        Online Banking
                                                    </a>
                                                </li>
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Branch Services" href="https://www.sc.com/hk/bank-with-us/branch-services/">
                                                        Branch Services
                                                    </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <!-- Services meganav Right side contents -->
                                        <div class="sc-mgdrop__right">
                                            <div class="sc-mgdrop__item-wrapper">
                                                <div class="sc-mgdrop__item">
                                                    <div class="sc-mgdrop__item-box">
                                                        <div class="sc-mgdrop__item-label">Mobile Banking</div>
                                                        <p class="sc-mgdrop__item-desc">
                                                            A more secure, simple and convenient mobile banking service
                                                        </p>
                                                        <a title="Mobile Banking" href="https://www.sc.com/hk/bank-with-us/app-sc-mobile/" class="sc-mgdrop__item-link">Learn More</a>
                                                    </div>
                                                    <a title="Mobile Banking" href="https://www.sc.com/hk/bank-with-us/app-sc-mobile/" class="sc-mgdrop__item-link only-mobile">
                                                        Mobile Banking
                                                    </a>
                                                </div>
                                                <div class="sc-mgdrop__item">
                                                    <div class="sc-mgdrop__item-box">
                                                        <div class="sc-mgdrop__item-label">Digital Banking services
                                                        </div>
                                                        <p class="sc-mgdrop__item-desc">
                                                            SC Mobile and Online Banking service guide
                                                        </p>
                                                        <a title="Digital Banking services" href="https://www.sc.com/hk/bank-with-us/standard-chartered-digital-banking/" class="sc-mgdrop__item-link">Learn More</a>
                                                    </div>
                                                    <a title="Digital Banking services" href="https://www.sc.com/hk/bank-with-us/standard-chartered-digital-banking/" class="sc-mgdrop__item-link only-mobile">
                                                        Digital Banking services
                                                    </a>
                                                </div>
                                                <div class="sc-mgdrop__item">
                                                    <div class="sc-mgdrop__item-box">
                                                        <div class="sc-mgdrop__item-label">Payments and Transfers</div>
                                                        <p class="sc-mgdrop__item-desc">
                                                            Transforming your payment experience through our digital
                                                            innovations
                                                        </p>
                                                        <a title="Payments and Transfers" data-context="Meganav Services Links" href="https://www.sc.com/hk/bank-with-us/payments-and-transfers/" class="sc-mgdrop__item-link">View Details</a>
                                                    </div>
                                                    <a title="Payments and Transfers" href="https://www.sc.com/hk/bank-with-us/payments-and-transfers/?intcid=servicestab-jul21-paymen" class="sc-mgdrop__item-link only-mobile">
                                                        Payments and Transfers
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- View all button -->
                                    <div class="sc-nav-drop__view-all">
                                        <a href="https://www.sc.com/hk/bank-with-us/" class="sc-nav-drop__btn">
                                            View All Services
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- Help -->
                <li class="sc-nav__item sc-nav__item--has-meganav">
                    <button class="sc-nav__btn sc-nav__menu">
                        Help
                    </button>
                    <div class="sc-nav__mgnv-wrapper">
                        <div class="sc-nav-drop">
                            <button class="sc-nav__btn sc-nav-drop__back sc-nav__back only-mobile">
                                Back
                            </button>
                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container">
                                    <div class="sc-mgdrop">
                                        <!-- Services meganav Left side contents -->
                                        <div class="sc-mgdrop__left">
                                            <span class="sc-mgdrop__title">Problems?
                                                <br>
                                                Visit our
                                                <a href="https://www.sc.com/hk/help/" target="_blank" rel="noopener noreferrer">help centre</a>
                                            </span>
                                            <ul class="sc-mgdrop__list">
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Chat with us" href="https://www.sc.com/hk/help/chat-with-us/">
                                                        Chat with us
                                                    </a>
                                                </li>
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Service Charges" href="https://www.sc.com/hk/help/service-charges/">
                                                        Service Charges
                                                    </a>
                                                </li>
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="FAQ" href="https://www.sc.com/hk/help/#sc-lb-module-product-features-1">
                                                        FAQ
                                                    </a>
                                                </li>
												<li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Fraud and Cyber Security" href="https://www.sc.com/hk/cybersecurity/">
                                                        Fraud and Cyber Security
                                                    </a>
                                                </li>
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Terms and Conditions" href="https://www.sc.com/hk/help/customer-terms-and-conditions/">
                                                        Terms and Conditions
                                                    </a>
                                                </li>
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Accessibility" href="https://www.sc.com/hk/help/accessibility/">
                                                        Accessibility
                                                    </a>
                                                </li>
                                                <li class="sc-mgdrop__list-item">
                                                    <a class="sc-mgdrop__list-item-link" title="Barrier-free Banking Services" href="https://www.sc.com/hk/help/barrier-free-banking-services/">
                                                        Barrier-free Banking Services
                                                    </a>
                                                </li>

                                            </ul>
                                        </div>
                                        <!-- Services meganav Right side contents -->
                                        <div class="sc-mgdrop__right">
                                            <div class="sc-mgdrop__item-wrapper">
                                                <div class="sc-mgdrop__item">
                                                    <div class="sc-mgdrop__item-box">
                                                        <div class="sc-mgdrop__item-label">Find a branch</div>
                                                        <p class="sc-mgdrop__item-desc">
                                                            And your nearest ATM locations
                                                        </p>
                                                        <a title="Find a branch" data-context="Meganav Services Links" href="https://www.sc.com/hk/atm-branch-locator/" class="sc-mgdrop__item-link">Learn More</a>
                                                    </div>
                                                    <a title="Find a branch" href="https://www.sc.com/hk/atm-branch-locator/" class="sc-mgdrop__item-link only-mobile">
                                                        Find a branch
                                                    </a>
                                                </div>
                                                <div class="sc-mgdrop__item">
                                                    <div class="sc-mgdrop__item-box">
                                                        <div class="sc-mgdrop__item-label">Forms and downloads</div>
                                                        <p class="sc-mgdrop__item-desc">
                                                            Download forms and documents
                                                        </p>
                                                        <a title="Forms and downloads" href="https://www.sc.com/hk/help/download-centre/" class="sc-mgdrop__item-link">Learn More</a>
                                                    </div>
                                                    <a title="Forms and downloads" href="https://www.sc.com/hk/help/download-centre/" class="sc-mgdrop__item-link only-mobile">
                                                        Forms and downloads
                                                    </a>
                                                </div>
                                                <div class="sc-mgdrop__item">
                                                    <div class="sc-mgdrop__item-box">
                                                        <div class="sc-mgdrop__item-label">Contact us</div>
                                                        <p class="sc-mgdrop__item-desc">
                                                            Write, call or send us a message
                                                        </p>
                                                        <a title="Contact us" href="https://www.sc.com/hk/help/contact-us/#sc-lb-module-need-module-1" class="sc-mgdrop__item-link">Learn More</a>
                                                    </div>
                                                    <a title="FAQ" href="https://www.sc.com/hk/help/contact-us/#sc-lb-module-need-module-1" class="sc-mgdrop__item-link only-mobile">
                                                        Contact us
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- View all button -->
                                    <div class="sc-nav-drop__view-all">
                                        <a href="https://www.sc.com/hk/help/" class="sc-nav-drop__btn">
                                            View All Help
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>

                <!-- This below list is added for creating line in mobile  -->
                <li class="sc-nav__line only-mobile"></li>

                <!-- Mobile screen - Services, Help, Search and country selector menu below -->
                <!--  <li class="sc-nav__item sc-nav__item--has-meganav only-mobile">
                     <a href="" class="sc-nav__btn sc-nav__menu" title="Services">Services</a>
                 </li>
                 <li class="sc-nav__item sc-nav__item--has-meganav only-mobile">
                     <a href="" class="sc-nav__btn sc-nav__menu" title="Help">Help</a>
                 </li>  -->
                <li class="sc-nav__item sc-nav__item--has-meganav only-mobile">
                    <a href="/hk/search/" title="Search" class="sc-nav__btn sc-nav__menu sc-nav__menu-search">
                        Search
                        <span class="sc-nav__icon only-mobile">
                            <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                                <defs>
                                    <path d="M15.33 15.142H0V0h15.33z"></path>
                                </defs>
                                <path d="M6.34 10.903A4.567 4.567 0 0 1 1.778 6.34 4.568 4.568 0 0 1 6.34 1.777a4.569 4.569 0 0 1 4.564 4.564 4.567 4.567 0 0 1-4.564 4.562m8.73 2.721l-3.596-3.592a6.283 6.283 0 0 0 1.208-3.691A6.348 6.348 0 0 0 6.34 0 6.348 6.348 0 0 0 0 6.34a6.347 6.347 0 0 0 6.34 6.34c1.476 0 2.816-.526 3.895-1.374l3.577 3.575a.887.887 0 0 0 1.257 0 .89.89 0 0 0 0-1.257" fill="#221F20" mask="url(#b)" transform="translate(.584)"></path>
                            </svg>
                        </span>
                    </a>
                </li>

                <li class="sc-nav__item sc-nav__item--has-meganav only-mobile">
                    <div class="sc-nav__top-right">
                        <div class="sc-nav__country">
                            <button class="sc-nav__country-btn">
                                Hong Kong
                            </button>
                        </div>
                        <div data-catch="update-language" data-language-sel="en" class="sc-nav__lang c-language-selector">
                            <button class="sc-nav__btn sc-nav__lang-link" data-send="update-language" data-language="zh">
                                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                                    <path d="M16.006 0.003c-6.402-0.001-12.188 3.815-14.708 9.7l-0.199 0.066 0.077 0.232c-3.318 8.183 0.626 17.506 8.809 20.823 1.911 0.775 3.954 1.173 6.016 1.172 8.835 0.001 15.998-7.16 15.999-15.994s-7.16-15.998-15.994-15.999zM28.553 24.065l-0.821-0.821v-1.912c0.001-0.083-0.017-0.164-0.053-0.238l-2.080-4.153v-2.007c0-0.178-0.089-0.345-0.237-0.444l-1.6-1.066c-0.125-0.084-0.28-0.11-0.427-0.074l-1.959 0.489-3.291-1.412-0.453-3.172 1.255-1.254h2.693l0.906 1.362c0.082 0.123 0.211 0.206 0.356 0.23l3.199 0.533c0.086 0.014 0.174 0.007 0.256-0.020l2.947-0.982c2.471 4.743 2.207 10.447-0.692 14.941zM26.354 5.258l-0.867 0.578-2.417-0.484-1.568-0.522c-0.096-0.033-0.199-0.037-0.298-0.012l-1.983 0.495-0.869-0.29 0.644-1.288h1.803c0.083 0 0.164-0.019 0.238-0.056l1.845-0.922c1.271 0.663 2.439 1.505 3.471 2.5zM10.161 2.26l1.28 0.853c0.063 0.042 0.134 0.070 0.209 0.082l2.584 0.431-0.252 0.754-1.346 0.45c-0.121 0.040-0.223 0.122-0.288 0.231l-1.531 2.552-2.46 1.476-3.626 0.518c-0.263 0.037-0.458 0.262-0.459 0.527v1.6c0 0.141 0.056 0.277 0.156 0.377l0.91 0.91v0.916l-2.218-1.479-0.805-2.414c1.531-3.498 4.337-6.281 7.847-7.784zM8.642 19.743l-2.41-0.483-0.896-1.787v-1.253l1.987-1.987 0.735 1.471c0.090 0.181 0.275 0.295 0.477 0.295h3.431l1.444 2.407c0.096 0.16 0.27 0.259 0.457 0.259h1.482l-0.373 1.87-2.019 2.019c-0.1 0.1-0.157 0.235-0.157 0.377v1.333l-1.92 1.44c-0.134 0.101-0.213 0.259-0.213 0.427v1.926l-0.663-0.22-0.936-2.342v-5.23c0-0.253-0.178-0.472-0.427-0.523zM7.040 27.94c-5.028-3.772-7.154-10.289-5.318-16.3l0.443 1.329c0.037 0.112 0.111 0.209 0.21 0.275l2.658 1.772-0.606 0.607c-0.1 0.1-0.156 0.236-0.156 0.377v1.6c-0 0.083 0.019 0.164 0.056 0.238l1.066 2.133c0.074 0.147 0.212 0.252 0.373 0.284l2.24 0.447v4.896c-0 0.068 0.013 0.135 0.038 0.198l1.066 2.666c0.058 0.146 0.178 0.258 0.327 0.308l1.6 0.533c0.053 0.018 0.109 0.027 0.166 0.028 0.294 0 0.533-0.239 0.533-0.533v-2.399l1.92-1.44c0.134-0.101 0.213-0.259 0.213-0.427v-1.379l1.977-1.977c0.074-0.074 0.125-0.169 0.146-0.272l0.533-2.666c0.058-0.289-0.13-0.57-0.418-0.627-0.034-0.007-0.069-0.010-0.104-0.010h-1.831l-1.444-2.408c-0.096-0.16-0.27-0.259-0.457-0.259h-3.403l-0.916-1.838c-0.077-0.153-0.223-0.261-0.392-0.288-0.169-0.029-0.342 0.027-0.462 0.149l-0.692 0.689v-0.846c0-0.141-0.056-0.277-0.156-0.377l-0.91-0.91v-0.917l3.275-0.468c0.070-0.010 0.138-0.034 0.199-0.071l2.666-1.6c0.075-0.045 0.137-0.108 0.182-0.182l1.498-2.497 1.412-0.471c0.159-0.052 0.285-0.177 0.337-0.337l0.533-1.6c0.092-0.28-0.059-0.581-0.339-0.674-0.026-0.009-0.052-0.015-0.079-0.020l-3.086-0.515-0.542-0.362c3.356-1.092 6.99-0.957 10.255 0.381l-0.974 0.486h-2.007c-0.203-0.001-0.389 0.113-0.48 0.295l-1.066 2.133c-0.131 0.264-0.024 0.584 0.239 0.715 0.022 0.011 0.046 0.021 0.069 0.029l1.6 0.533c0.096 0.033 0.199 0.037 0.298 0.012l1.983-0.495 1.453 0.484c0.021 0.007 0.042 0.013 0.064 0.017l2.666 0.533c0.139 0.028 0.283-0 0.4-0.079l1.214-0.809c0.597 0.665 1.134 1.382 1.604 2.143l-2.623 0.874-2.84-0.473-0.938-1.408c-0.098-0.147-0.264-0.236-0.441-0.237h-3.199c-0.141 0-0.277 0.056-0.377 0.156l-1.6 1.6c-0.119 0.119-0.175 0.286-0.151 0.453l0.533 3.733c0.027 0.185 0.148 0.342 0.32 0.414l3.733 1.6c0.107 0.046 0.226 0.056 0.339 0.027l1.904-0.476 1.164 0.777v1.848c-0.001 0.083 0.017 0.164 0.053 0.238l2.080 4.153v2.007c0 0.141 0.056 0.277 0.156 0.377l1.116 1.116c-4.947 6.594-14.303 7.929-20.898 2.982z">
                                    </path>
                                </svg>

                                中文
                            </button>
                        </div>
                    </div>
                </li>
                <!-- This below list is added for creating overlay effect via css.  -->
                <li class="sc-nav__overlay only-desktop"></li>
            </ul>
            <div class="sc-nav__login-open-btn">
                <!-- Open an account Button -->
                <!--<div class="sc-nav__open-account">
  <a
  class="sc-nav__btn sc-nav__account-btn"
  title="Open an account"
  href="/hk/banking/sc-mobile/"
  >
  <span class="icon">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 30">
    <path
      fill="#00a546"
      d="M1 30c-.6 0-1-.4-1-1v-5.1c0-1.3 1.2-2.7 2.1-3.1l5.7-2.3c.5-.2.7-.4.8-.6.2-.5.8-.7 1.3-.5.5.2.7.8.5 1.3-.4 1-1.4 1.4-1.8 1.6l-.2.1-5.7 2.2c-.2.3-.7 1-.7 1.3V29c0 .5-.4 1-1 1zM23 30c-.6 0-1-.4-1-1v-5.1c0-.4-.4-1.1-.6-1.2l-5.8-2.3c-.5-.2-1.5-.6-2-1.6-.2-.5 0-1.1.5-1.3.5-.2 1.1 0 1.3.5 0 .1.2.2.9.5.1 0 .1.1.2.1l5.6 2.2c.9.3 1.8 1.8 1.8 3.1V29c.1.5-.3 1-.9 1zM13 16h-1.7c-2 0-4-2.2-4.6-5.1v-.1L6 5.7C6 2.5 8.5 0 11.6 0h1.5c2.9.2 5.2 2.7 5.2 5.6v.1l-.7 5C17 13.7 15 16 13 16zm-4.4-5.6c.5 2.2 1.9 3.5 2.7 3.5H13c.8 0 2.2-1.4 2.7-3.5l.6-4.8c0-1.9-1.5-3.4-3.4-3.6h-1.3C9.6 2 8 3.6 8 5.6l.6 4.8zm8.7-4.7z"
    ></path>
    </svg>
  </span>
  Open an account
  </a>
</div>-->

                <!-- Login Buttons -->
                <div class="sc-nav__login sc-nav__login--full">
                    <button class="sc-nav__btn sc-nav__login-btn" title="Login" aria-expanded="false">
                        <span class="sc-nav__icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="15" viewBox="0 0 24.19 28.58">
                                <g data-name="Layer 2">
                                    <g>
                                        <path d="M21.19 28.58H3a3 3 0 0 1-3-3V11.23a3 3 0 0 1 3-3h18.19a3 3 0 0 1 3 3v14.35a3 3 0 0 1-3 3zM3 10.23a1 1 0 0 0-1 1v14.35a1 1 0 0 0 1 1h18.19a1 1 0 0 0 1-1V11.23a1 1 0 0 0-1-1z" fill="#d4d4d4"></path>
                                        <path d="M19 9.43a1 1 0 0 1-1-1v-2.7A3.74 3.74 0 0 0 14.26 2H9.92a3.74 3.74 0 0 0-3.73 3.73v2.7a1 1 0 0 1-2 0v-2.7A5.74 5.74 0 0 1 9.92 0h4.34A5.74 5.74 0 0 1 20 5.73v2.7a1 1 0 0 1-1 1zM12.19 23.33a.5.5 0 0 1-.5-.5v-4a.5.5 0 0 1 1 0v4a.5.5 0 0 1-.5.5z" fill="#d4d4d4"></path>
                                        <path d="M12.12 18.93a2 2 0 1 1 2-2 2 2 0 0 1-2 2zm0-2.44a.47.47 0 1 0 .47.47.47.47 0 0 0-.47-.47z" fill="#d4d4d4" data-name="Ellipse 7"></path>
                                        <path d="M12.12 18.93a2 2 0 1 1 2-2 2 2 0 0 1-2 2zm0-2.44a.47.47 0 1 0 .47.47.47.47 0 0 0-.47-.47z" fill="#d4d4d4" data-name="Ellipse 7"></path>
                                    </g>
                                </g>
                            </svg>
                        </span>
                        Login
                    </button>
                    <!-- Login New Dropdown  -->
<div class="sc-login-drop">
                        <span class="sc-login-drop__title only-mobile">
                            Welcome to Standard Chartered
                        </span>
                        <div class="sc-nav-drop">
                            <div class="sc-nav-drop__content">
                                <div class="sc-nav-drop__wrapper sc-nav__container only-desktop-login">
                                    <div class="sc-nav-drop__col-wrapper">
                                        <div class="sc-nav-drop__col-20">
                                            <div class="sc-nav-drop__col">
												<a title="Refer and earn rewards" href="https://www.sc.com/hk/promotions/refer-and-earn/?intcid=leg_nav-sc_com-login_button-mgm-desktop_hk-en">
													<div class="sc-nav-drop__promo-box">
														<img aria-hidden="true" src="https://av.sc.com/hk/content/images/hk-nav-mgm-560-280.jpg" alt="Refer and earn rewards">
														<div class="sc-nav-drop__promo-text">
															<p class="sc-nav-drop__promo-title">
																Refer and earn rewards
															</p>
															<p class="sc-nav-drop__promo-desc">
																Download SC Mobile App to start sharing to earn
															</p>
														</div>
													</div>
												</a>
											</div>
                                        </div>
                                        <div class="sc-nav-drop__col-80">
                                            <div class="sc-nav-drop__col-100">
                                                <div class="sc-nav-drop__col" style="width:70%">
                                                    <div href="#" class="sc-nav__login-lists-box" id="sc_nav_clients">
														<h4 style="color: #0c77b9; font-size: 22px; margin-bottom: 20px;line-height: 22px;font-weight: 700; text-align:center">Retail Banking Clients</h4>
														<div style="display:block">
															<p style="text-align:center" id="sc_nav_clients_title">Scan the QR code below to login to SC Mobile App </p>                                
														</div>
														<div style="display:flex;justify-content: center;">
															<div style="width:30%">
																<img src="https://av.sc.com/hk/content/images/hk-nav-scmobile-qrcode-en.png" style="display:block; margin: 0 auto; width:100%">
															</div>
															<div style="width:30%; margin: auto 0;">
																<img src="https://av.sc.com/hk/zh/others/hk-nav-mobile-appstore.svg" style="display:block; margin: 8px auto; width:70%">
																<img src="https://av.sc.com/hk/content/images/hk-nav-mobile-playstore.png" style="display:block; margin: 8px auto; width:70%">
																<img src="https://av.sc.com/hk/others/hk-nav-mobile-huawei.svg" style="display:block; margin: 8px auto; width:70%">
																
															</div>   
														</div>
														<br>
														
                                                        <div style="display: flex;justify-content: space-around;">
															<button class="sc-nav__btn sc-nav__login-btn sc_nav_channel_button" id="sc_nav_channel_button_1" title="Login to Online Banking" aria-expanded="false" style="width: 40%; height: 60px; font-size:16px; background: #fff; border-radius:25px;">
																<a id="sc_nav_channel_button_a" href="https://www.sc.com/hk/ibk-redirect/" title="Login to Online Banking">Login to Online Banking</a>
															</button>
															<button class="sc-nav__btn sc-nav__login-btn sc_nav_channel_button" id="sc_nav_channel_button_2" title="Login to Online Securities" aria-expanded="false" style="width: 40%; height: 60px; font-size:16px;background: #fff; border-radius:25px;">
																<a id="sc_nav_channel_button_a" href="https://wealth.sc.com/wm/full/hk/oe/desktop/#!/login?lang=en_HK" title="Login to Online Securities">Login to Online Securities</a>
															</button>
														</div>
                                                    </div>
                                                </div>
                                                <div class="sc-nav-drop__col" style="width:30%;display: flex;flex-direction: column;">
                                                    
<div class="sc-nav__login-lists-box" id="sc_nav_clients" style="height:50%;display: flex;flex-direction: column;justify-content: center;">
                                                        <div class="sc-nav__login-lists-box-title" style="display:block;">
                                                            <h4 style="color: #0c77b9; font-size: 22px; line-height: 22px;font-weight: 700; text-align:center;">SME Banking Clients</h4>
                                                        </div>

                                                        <div style="display: flex;justify-content: center;">
															<button class="sc-nav__btn sc-nav__login-btn sc_nav_channel_button" id="sc_nav_channel_button_3" title="Login to Straight2Bank" aria-expanded="false" style="width: 90%; height: 60px; background: #fff; border-radius:25px;">
																<a href="https://s2b.standardchartered.com/unifiedlogin/login/index.html?utm_source=sc.com-hk-en&amp;utm_medium=login-widget-menu-item&amp;utm_campaign=sc-retail-traffic" id="sc_nav_channel_button_a" style="font-size:16px" title="Login to Straight2Bank">Login to Straight2Bank</a>
															</button>
														</div>
                                                    </div><div class="sc-nav__login-lists-box" id="sc_nav_clients" style="height:50%;display: flex;flex-direction: column;justify-content: center;">
                                                        <div class="sc-nav__login-lists-box-title" style="
    display:block;
">
                                                            <h4 style="color: #0c77b9; font-size: 22px; line-height: 22px;font-weight: 700; text-align:center;">360° Rewards</h4>
                                                        </div>
																							
                                                        <div style="display: flex;justify-content: center;">
															<button class="sc-nav__btn sc-nav__login-btn sc_nav_channel_button" id="sc_nav_channel_button_4" title="360° Rewards" aria-expanded="false" style="width: 90%; height: 60px; background: #fff; border-radius:25px;">
																<a href="https://www.sc.com/hk/promotions/credit-cards/new-reward-redemption/" id="sc_nav_channel_button_a" style="font-size:16px; text-transform:initial;" title="360° Rewards">Learn more</a>
															</button>
														</div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
								<div class="sc-nav-drop__wrapper sc-nav__container only-mobile-login">
                                    <div class="sc-nav-drop__col-wrapper" style="width:100%">
                                        <div class="sc-nav-drop__col-20">
                                            <div class="sc-nav-drop__col">
                                                <a title="Refer and earn rewards" href="https://www.sc.com/hk/promotions/refer-and-earn/?intcid=leg_nav-sc_com-login_button-mgm-desktop_hk-en">
													<div class="sc-nav-drop__promo-box">
														<img aria-hidden="true" src="https://av.sc.com/hk/content/images/hk-nav-mgm-560-280.jpg" alt="Refer and earn rewards">
														<div class="sc-nav-drop__promo-text">
															<p class="sc-nav-drop__promo-title">
																Refer and earn rewards
															</p>
															<p class="sc-nav-drop__promo-desc">
																Download SC Mobile App to start sharing to earn
															</p>
														</div>
													</div>
												</a>
                                            </div>
                                        </div>
                                        <div class="sc-nav-drop__col-80">
                                            <div class="sc-nav-drop__col-100">
                                                
                                                <div class="sc-nav-drop__col">
                                                    <a href="https://retail.sc.com/scmobile/hk" title="SC Mobile App Login" class="sc-nav__login-lists-box">
                                                        <div class="sc-nav__login-lists-box-icon">
                                                            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 64 64">
                                                                <title>mobile</title>
                                                                <path fill="#38d200" d="M27.878 47.561v2.439c0 2.209 1.791 4 4 4h13.463c2.209 0 4-1.791 4-4v-26.341c0-2.209-1.791-4-4-4h-5.659v23.902c0 2.209-1.791 4-4 4h-7.805z">
                                                                </path>
                                                                <path fill="#0f7aed" d="M15 14c0-2.209 1.791-4 4-4h13.463c2.209 0 4 1.791 4 4l0.037 8.5-9.553 3.847-5.616 1.664-6.331 6.647v-20.659z">
                                                                </path>
                                                                <path fill="#0f7aed" d="M36.463 22.487v17.854c0 2.209-1.791 4-4 4h-13.463c-2.209 0-4-1.791-4-4v-5.683l6.331-6.647 5.616-1.664 9.517-3.86zM25.732 42.195c1.185 0 2.146-0.961 2.146-2.146s-0.961-2.146-2.146-2.146c-1.185 0-2.146 0.961-2.146 2.146s0.961 2.146 2.146 2.146z">
                                                                </path>
                                                            </svg>
                                                        </div>

                                                        <div class="sc-nav__login-lists-box-title">
                                                            SC Mobile App Login
                                                        </div>
                                                        <div class="sc-nav__login-lists-box-content">
                                                            
                                                        </div>
                                                    </a>
                                                </div>
												<div class="sc-nav-drop__col">
                                                    <a href="https://www.sc.com/hk/ibk-redirect/" title="Online Banking Login" class="sc-nav__login-lists-box">
                                                        <div class="sc-nav__login-lists-box-icon">
                                                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                                <path d="M3.75 15.75H19.875C19.875 17.4069 18.5319 18.75 16.875 18.75H6.75C5.09315 18.75 3.75 17.4069 3.75 15.75Z" fill="#38D200"></path>
                                                                <path d="M11.1941 5.25H7.5C6.25736 5.25 5.25 6.25736 5.25 7.5V14.25H18.75V10.3357L17.8036 11.2443C16.9072 12.1049 15.4828 12.0758 14.6223 11.1794C14.1522 10.6897 13.9475 10.0424 14.0048 9.41559L12.375 9.41558C11.1324 9.41558 10.125 8.40822 10.125 7.16558C10.125 6.35604 10.5525 5.64636 11.1941 5.25Z" fill="#0F7AED"></path>
                                                                <path fillrule="evenodd" cliprule="evenodd" d="M15.0749 3.7045C15.5142 3.26517 16.2266 3.26517 16.6659 3.7045L20.113 7.15165L19.2238 8.0409L16.6659 10.5988C16.2266 11.0381 15.5142 11.0381 15.0749 10.5988C14.6356 10.1595 14.6356 9.44715 15.0749 9.00781L15.7123 8.3704L12.375 8.3704C11.7537 8.3704 11.25 7.86672 11.25 7.2454C11.25 6.62408 11.7537 6.1204 12.375 6.1204L15.8998 6.1204L15.0749 5.2955C14.6356 4.85616 14.6356 4.14384 15.0749 3.7045Z" fill="#38D200"></path>
                                                            </svg>
                                                        </div>

                                                        <div class="sc-nav__login-lists-box-title">
                                                            Online Banking Login
                                                        </div>
                                                        <div class="sc-nav__login-lists-box-content">
                                                            
                                                        </div>
                                                    </a>
                                                </div>

                                                <div class="sc-nav-drop__col">
                                                    <a href="https://wealth.sc.com/wm/full/hk/oe/desktop/#!/login?lang=en_HK" title=" Online Securities" class="sc-nav__login-lists-box">
                                                        <div class="sc-nav__login-lists-box-icon">
                                                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                                <path fillrule="evenodd" cliprule="evenodd" d="M11.8126 1.875C12.2842 1.875 12.7058 2.16923 12.8685 2.61195L14.4181 6.82877L18.8023 7.03276C19.2679 7.05442 19.672 7.36095 19.8182 7.8035C19.9645 8.24606 19.8227 8.73298 19.4617 9.02783L16.0123 11.8453L17.1865 16.2076C17.3086 16.661 17.1361 17.1426 16.754 17.4155C16.3719 17.6884 15.8604 17.6953 15.4711 17.4327L11.8126 14.9651L8.15401 17.4327C7.76471 17.6953 7.25326 17.6884 6.87112 17.4155C6.48899 17.1426 6.31656 16.661 6.43861 16.2076L7.6128 11.8453L4.16338 9.02783C3.8024 8.73298 3.66062 8.24606 3.80689 7.8035C3.95315 7.36095 4.35717 7.05442 4.82277 7.03276L9.20698 6.82877L10.7566 2.61195C10.9193 2.16923 11.3409 1.875 11.8126 1.875ZM11.8126 6.2615L11.0613 8.30589C10.9052 8.73069 10.5097 9.02059 10.0576 9.04163L7.8621 9.14378L9.60005 10.5633C9.9432 10.8436 10.0899 11.2992 9.97472 11.727L9.39468 13.8819L11.1835 12.6754C11.5637 12.419 12.0614 12.419 12.4416 12.6754L14.2304 13.8819L13.6504 11.727C13.5352 11.2992 13.6819 10.8436 14.0251 10.5633L15.763 9.14378L13.5675 9.04163C13.1154 9.02059 12.72 8.73069 12.5638 8.30589L11.8126 6.2615Z" fill="#0F7AED"></path>
                                                                <path fillrule="evenodd" cliprule="evenodd" d="M12 21.75C11.1716 21.75 10.5 21.0784 10.5 20.25C10.5 19.4216 11.1716 18.75 12 18.75C12.8284 18.75 13.5 19.4216 13.5 20.25C13.5 21.0784 12.8284 21.75 12 21.75Z" fill="#38D200"></path>
                                                            </svg>
                                                        </div>

                                                        <div class="sc-nav__login-lists-box-title">
                                                            Online Securities
                                                        </div>
                                                        <div class="sc-nav__login-lists-box-content">
                                                            
                                                        </div>
                                                    </a>
                                                </div>
                                            </div>
                                            <div class="sc-nav-drop__col-100">
                                                
                                                <div class="sc-nav-drop__col">
                                                    <a href="https://www.sc.com/hk/promotions/credit-cards/new-reward-redemption/" title="360° Rewards" class="sc-nav__login-lists-box">
                                                        <div class="sc-nav__login-lists-box-icon">
                                                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                                <path fillrule="evenodd" cliprule="evenodd" d="M14.6195 4.5C12.3129 4.5 11.8187 5.75397 11.8187 7.30083V8.21277C11.6217 8.32672 11.4891 8.53969 11.4891 8.78362V9.77215C11.4891 10.1076 11.7398 10.3845 12.064 10.4258C12.205 10.7394 12.4021 11.0223 12.6424 11.2618V13.0672L9.56135 15.2273C8.60744 15.8314 8.0293 16.8819 8.0293 18.0111V18.6689H13.7957L14.2307 15.624C13.878 15.473 13.631 15.1228 13.631 14.7148C13.631 14.1689 14.0735 13.7263 14.6195 13.7263C15.1654 13.7263 15.608 14.1689 15.608 14.7148C15.608 15.1157 15.3694 15.4608 15.0265 15.616L15.608 18.6689H21.3744V17.9781C21.3744 16.867 20.8145 15.8307 19.8851 15.2218L16.5965 13.0672V11.2618C16.8369 11.0223 17.034 10.7394 17.175 10.4258C17.4992 10.3845 17.7498 10.1076 17.7498 9.77215V8.78362C17.7498 8.53969 17.6173 8.32672 17.4203 8.21277V7.30083C17.4203 5.75397 16.9261 4.5 14.6195 4.5Z" fill="#0F7AED"></path>
                                                                <path fillrule="evenodd" cliprule="evenodd" d="M9.59019 4.5C7.28362 4.5 6.78936 5.75397 6.78936 7.30083V8.21277C6.59238 8.32672 6.45985 8.53969 6.45985 8.78362V9.77215C6.45985 10.1076 6.71046 10.3845 7.03466 10.4258C7.17572 10.7394 7.3728 11.0223 7.61313 11.2618V13.0672L4.53205 15.2273C3.57814 15.8314 3 16.8819 3 18.0111V18.6689H6.25681V18.0173C6.25681 16.8989 6.82947 15.8584 7.77434 15.2599L10.8262 13.1204V11.332C10.5882 11.0948 10.393 10.8146 10.2532 10.504C9.93211 10.463 9.68387 10.1888 9.68387 9.85649V8.87733C9.68387 8.63571 9.81514 8.42475 10.0103 8.31189V7.40859C10.0103 6.27986 10.276 5.30857 11.3293 4.8753C10.9154 4.63662 10.3515 4.5 9.59019 4.5Z" fill="#38D200"></path>
                                                            </svg>
                                                        </div>

                                                        <div class="sc-nav__login-lists-box-title">
                                                            360° Rewards
                                                        </div>
                                                        <div class="sc-nav__login-lists-box-content">
                                                            
                                                        </div>
                                                    </a>
                                                </div>
                                                <div class="sc-nav-drop__col">
                                                    <a href="https://s2b.standardchartered.com/unifiedlogin/login/index.html?utm_source=sc.com-hk-en&amp;utm_medium=login-widget-menu-item&amp;utm_campaign=sc-retail-traffic " title="  Straight2Bank Login" class="sc-nav__login-lists-box">
                                                        <div class="sc-nav__login-lists-box-icon">
                                                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                                <path d="M15.75 20.25V7.5C15.75 6.67157 16.4216 6 17.25 6C18.0784 6 18.75 6.67157 18.75 7.5V20.25H15.75Z" fill="#38D200"></path>
                                                                <path fillrule="evenodd" cliprule="evenodd" d="M10.5 20.25V12C10.5 11.1716 11.1716 10.5 12 10.5C12.8284 10.5 13.5 11.1716 13.5 12V20.25H10.5Z" fill="#0F7AED"></path>
                                                                <path d="M8.25 20.25H5.25L5.25 14.625C5.25 13.7966 5.92157 13.125 6.75 13.125C7.57843 13.125 8.25 13.7966 8.25 14.625V20.25Z" fill="#38D200"></path>
                                                            </svg>
                                                        </div>

                                                        <div class="sc-nav__login-lists-box-title">
                                                            Straight2Bank Login
                                                        </div>
                                                        <div class="sc-nav__login-lists-box-content">
                                                            
                                                        </div>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Login Popup box links -->
                    <!-- <div class="sc-login-drop">
                        <span class="sc-login-drop__title only-mobile">Welcome to Standard Chartered</span>
                        <ul>
                            <li>
                                <a title="Online Banking Login" href="https://www.sc.com/hk/ibk-redirect/" class="sc-login-drop__link sc-login-drop__link-first" data-send="null" data-context="Meganav Links Online Banking Login">
                                    Online Banking Login
                                    <span class="sc-nav__icon">
                 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24.19 28.58">
                   <g data-name="Layer 2">
                     <g>
                       <path
                               d="M21.19 28.58H3a3 3 0 0 1-3-3V11.23a3 3 0 0 1 3-3h18.19a3 3 0 0 1 3 3v14.35a3 3 0 0 1-3 3zM3 10.23a1 1 0 0 0-1 1v14.35a1 1 0 0 0 1 1h18.19a1 1 0 0 0 1-1V11.23a1 1 0 0 0-1-1z"
                               fill="#d4d4d4"
                       ></path>
                       <path
                               d="M19 9.43a1 1 0 0 1-1-1v-2.7A3.74 3.74 0 0 0 14.26 2H9.92a3.74 3.74 0 0 0-3.73 3.73v2.7a1 1 0 0 1-2 0v-2.7A5.74 5.74 0 0 1 9.92 0h4.34A5.74 5.74 0 0 1 20 5.73v2.7a1 1 0 0 1-1 1zM12.19 23.33a.5.5 0 0 1-.5-.5v-4a.5.5 0 0 1 1 0v4a.5.5 0 0 1-.5.5z"
                               fill="#d4d4d4"
                       ></path>
                       <path
                               d="M12.12 18.93a2 2 0 1 1 2-2 2 2 0 0 1-2 2zm0-2.44a.47.47 0 1 0 .47.47.47.47 0 0 0-.47-.47z"
                               fill="#d4d4d4"
                               data-name="Ellipse 7"
                       ></path>
                       <path
                               d="M12.12 18.93a2 2 0 1 1 2-2 2 2 0 0 1-2 2zm0-2.44a.47.47 0 1 0 .47.47.47.47 0 0 0-.47-.47z"
                               fill="#d4d4d4"
                               data-name="Ellipse 7"
                       ></path>
                     </g>
                   </g>
                 </svg>
               </span>
                                </a>
                            </li>
                            <li>
                                <a title="Online Securities" href="https://wealth.sc.com/wm/full/hk/oe/desktop/#!/login?lang=en_HK" class="sc-login-drop__link" data-send="null" data-context="Meganav Links Online Securities">
                                    Online Securities
                                    <span class="sc-nav__icon">
                 <svg
                         xmlns="http://www.w3.org/2000/svg"
                         preserveAspectRatio="xMidYMid"
                         width="28"
                         height="26"
                         viewBox="0 0 28 26"
                 >
                   <image
                           href="data:img/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAaCAMAAACTisy7AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAPFBMVEUAAADU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NQAAAAamdYyAAAAEnRSTlMAJa3xJ++3GfPhw8TyGK61GyjofnilAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEgAACxIB0t1+/AAAAHxJREFUKM/V0tsKgCAQBNBptZtZ1vz/x2ZJ9/Uh6KUBFTy4gi5QiKESIwVgS2ZSWgirGkrqigJD1aKyAQm0t33nljnKgrwh+QZTqbQ+kDxOfYzbfSqex4/RddeR/ZX9rVKZR9oVfa5N+tgmA0Ov2Rg4YMq35hQbV7xGXixmgYwWLY107UoAAAAASUVORK5CYII="
                           width="28"
                           height="26"
                   ></image>
                 </svg>
               </span>
                                </a>
                            </li>
                            <li>
                                <a title="Credit Card Online" href="https://ibank.standardchartered.com.hk/nfs/login.htm?lang=en_US&_ga=2.87224600.1035095479.1613967437-1498348113.1608520554" class="sc-login-drop__link" data-send="null" data-context="Meganav Links Crdeit Card Online">
                                    Credit Card Online
                                    <span class="sc-nav__icon">
                 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24.19 28.58">
                   <g data-name="Layer 2">
                     <g>
                       <path
                               d="M21.19 28.58H3a3 3 0 0 1-3-3V11.23a3 3 0 0 1 3-3h18.19a3 3 0 0 1 3 3v14.35a3 3 0 0 1-3 3zM3 10.23a1 1 0 0 0-1 1v14.35a1 1 0 0 0 1 1h18.19a1 1 0 0 0 1-1V11.23a1 1 0 0 0-1-1z"
                               fill="#d4d4d4"
                       ></path>
                       <path
                               d="M19 9.43a1 1 0 0 1-1-1v-2.7A3.74 3.74 0 0 0 14.26 2H9.92a3.74 3.74 0 0 0-3.73 3.73v2.7a1 1 0 0 1-2 0v-2.7A5.74 5.74 0 0 1 9.92 0h4.34A5.74 5.74 0 0 1 20 5.73v2.7a1 1 0 0 1-1 1zM12.19 23.33a.5.5 0 0 1-.5-.5v-4a.5.5 0 0 1 1 0v4a.5.5 0 0 1-.5.5z"
                               fill="#d4d4d4"
                       ></path>
                       <path
                               d="M12.12 18.93a2 2 0 1 1 2-2 2 2 0 0 1-2 2zm0-2.44a.47.47 0 1 0 .47.47.47.47 0 0 0-.47-.47z"
                               fill="#d4d4d4"
                               data-name="Ellipse 7"
                       ></path>
                       <path
                               d="M12.12 18.93a2 2 0 1 1 2-2 2 2 0 0 1-2 2zm0-2.44a.47.47 0 1 0 .47.47.47.47 0 0 0-.47-.47z"
                               fill="#d4d4d4"
                               data-name="Ellipse 7"
                       ></path>
                     </g>
                   </g>
                 </svg>
               </span>
                                </a>
                            </li>
                            <li>
                                <a title="360° Rewards" href="https://www.sc.com/hk/promotions/credit-cards/new-reward-redemption/" class="sc-login-drop__link" data-send="null" data-context="Meganav Links Online Rewards">
                                    360° Rewards
                                    <span class="sc-nav__icon">
                 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.63 34.61">
                   <g data-name="Layer 2">
                     <g fill="#d4d4d4">
                       <path
                               d="M15.45 23.51A8.49 8.49 0 1 1 23.93 15a8.5 8.5 0 0 1-8.48 8.51zm0-16A7.49 7.49 0 1 0 22.93 15a7.5 7.5 0 0 0-7.48-7.46z"
                       ></path>
                       <path
                               d="M11.74 19.16a.6.6 0 0 1-.43-.19 5.72 5.72 0 0 1 0-7.94.6.6 0 0 1 .86.84 4.52 4.52 0 0 0 0 6.27.6.6 0 0 1-.43 1z"
                       ></path>
                       <path
                               d="M15.32 29.83L12 27.13l-4.3.72-1.51-4-4.1-1.47.71-4.18L0 14.92l2.8-3.28-.74-4.19L6.16 6l1.51-4 4.3.72L15.32 0l3.35 2.71L23 2l1.51 4 4.1 1.47-.74 4.19 2.8 3.28-2.8 3.28.74 4.19-4.1 1.47-1.51 4-4.3-.72zM12.53 25l2.79 2.26L18.1 25l3.57.6 1.25-3.31 3.38-1.22-.61-3.46 2.3-2.7-2.3-2.7.61-3.46-3.37-1.21-1.26-3.31-3.57.6-2.78-2.26-2.79 2.26L9 4.23 7.71 7.54 4.32 8.76l.61 3.46-2.3 2.7 2.3 2.7-.61 3.46L7.7 22.3 9 25.6z"
                       ></path>
                       <path
                               d="M23.32 34.61l-8-2.29-8 2.29v-4.32a1 1 0 0 1 2 0V32l6-1.71 6 1.71v-1.71a1 1 0 0 1 2 0z"
                       ></path>
                     </g>
                   </g>
                 </svg>
               </span>
                                </a>
                            </li>
                            <li>
                                <a title="Straight2Bank Login" href="https://s2b.standardchartered.com/unifiedlogin/login/index.html" class="sc-login-drop__link sc-login-drop__bank-login" data-send="null" data-context="Meganav Links Straight2Bank Login">
                                    Straight2Bank Login
                                    <span class="sc-nav__icon">
                 <svg
                         xmlns="http://www.w3.org/2000/svg"
                         preserveAspectRatio="xMidYMid"
                         width="28"
                         height="26"
                         viewBox="0 0 28 26"
                 >
                   <image
                           href="data:img/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAaCAMAAACTisy7AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAPFBMVEUAAADU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NQAAAAamdYyAAAAEnRSTlMAJa3xJ++3GfPhw8TyGK61GyjofnilAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEgAACxIB0t1+/AAAAHxJREFUKM/V0tsKgCAQBNBptZtZ1vz/x2ZJ9/Uh6KUBFTy4gi5QiKESIwVgS2ZSWgirGkrqigJD1aKyAQm0t33nljnKgrwh+QZTqbQ+kDxOfYzbfSqex4/RddeR/ZX9rVKZR9oVfa5N+tgmA0Ov2Rg4YMq35hQbV7xGXixmgYwWLY107UoAAAAASUVORK5CYII="
                           width="28"
                           height="26"
                   ></image>
                 </svg>
               </span>
                                </a>
                            </li>
                        </ul>
                    </div> -->
                </div>
                <div class="sc-nav__overlay only-desktop"></div>
            </div>
            <!-- Hamburger Menu: Visible only for mobile  -->
            <button class="sc-nav__btn sc-nav__close-button">
                <span class="visuallyhidden">Close button</span>
            </button>
            <button class="sc-nav__btn sc-nav__hamburger only-mobile">
                <svg width="26" height="21" viewBox="0 0 26 21" xmlns="http://www.w3.org/2000/svg">
                    <path d="M25.5 11H.5a.5.5 0 0 1 0-1h25a.5.5 0 0 1 0 1zm0-10H.5a.5.5 0 0 1 0-1h25a.5.5 0 0 1 0 1zM.5 20h25a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1z" fill="#B9B9B9"></path>
                </svg>
                <span class="visuallyhidden">Menu</span>
            </button>
        </nav>
    </div>

    <!-- Country List -->
    <div class="sc-modal c-modal is-visible">
        <div class="sc-modal__scroll">
            <div class="sc-modal__wrapper">
                <div class="sc-modal__content">
                    <div class="sc-country">
                        <button class="sc-nav__btn sc-nav-drop__back sc-country__js-btn">
                            <span class="visuallyhidden">Back button</span>
                        </button>
                        <div class="sc-country__search-box" data-size="auto">
                            <label class="sc-country__wrapper">
                                <input type="text" class="sc-country__input" name="country" placeholder="Enter your market" id="sc-country__input-2">
                                <span class="sc-country__icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="35.278" height="33.073" viewBox="2 2 35.278 33.073">
                                        <path fill="#cccccc" d="M15.94 28.88C8.797 28.88 3 23.082 3 15.94 3 8.798 8.901 3 15.94 3s12.94 5.798 12.94 12.94c0 7.142-5.798 12.94-12.94 12.94zm0-23.914c-6.004 0-10.87 4.866-10.87 10.974a10.915 10.915 0 0 0 10.974 10.974c6.107 0 10.87-4.97 10.87-10.974 0-6.004-4.865-10.974-10.974-10.974zm11.389 21.326l8.281 7.246m.517-.619l-8.281-7.248-1.035 1.139 8.281 7.246 1.035-1.137z">
                                        </path>
                                    </svg>
                                </span>
                            </label>
                        </div>
                        <div class="sc-country__list">
                            <ul class="sc-country__list-items">
                                <li class="sc-country__list-item" data-value="AGO">
                                    <a href="https://www.sc.com/ao/" class="sc-country__country-link" title="Angola" data-url-updated="true" data-url-updated-param="true">
                                        Angola
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="ARG">
                                    <a href="https://www.sc.com/ar-en/" class="sc-country__country-link" title="Argentina">
                                        Argentina
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="AUS">
                                    <a href="https://www.sc.com/au/" class="sc-country__country-link" title="Australia">
                                        Australia
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="BHR">
                                    <a href="https://www.sc.com/bh/" class="sc-country__country-link" title="Bahrain">
                                        Bahrain
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="BGD">
                                    <a href="https://www.sc.com/bd/" class="sc-country__country-link" title="Bangladesh">
                                        Bangladesh
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="BWA">
                                    <a href="https://www.sc.com/bw/" class="sc-country__country-link" title="Botswana">
                                        Botswana
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="BRA">
                                    <a href="https://www.sc.com/br-en/" class="sc-country__country-link" title="Brazil">
                                        Brazil
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="BRN">
                                    <a href="https://www.sc.com/bn/en/" class="sc-country__country-link" title="Brunei Darussalam">
                                        Brunei Darussalam
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="KHM">
                                    <a href="https://www.sc.com/kh/" class="sc-country__country-link" title="Cambodia">
                                        Cambodia
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="CMR">
                                    <a href="https://www.sc.com/cm/" class="sc-country__country-link" title="Cameroon">
                                        Cameroon
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="CHL">
                                    <a href="https://www.sc.com/ar-en/" class="sc-country__country-link" title="Chile">
                                        Chile
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="CHN">
                                    <a href="https://www.sc.com/cn/" class="sc-country__country-link" title="China">
                                        China
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="COL">
                                    <a href="https://www.sc.com/co-en/" class="sc-country__country-link" title="Colombia">
                                        Colombia
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="FLK">
                                    <a href="https://www.sc.com/fk/" class="sc-country__country-link" title="Falkland Islands">
                                        Falkland Islands
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="FRA">
                                    <a href="https://www.sc.com/fr-en/" class="sc-country__country-link" title="France">
                                        France
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="DEU">
                                    <a href="https://www.sc.com/de-en/" class="sc-country__country-link" title="Germany">
                                        Germany
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="GHA">
                                    <a href="https://www.sc.com/gh/" class="sc-country__country-link" title="Ghana">
                                        Ghana
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="HKG">
                                    <a href="https://www.sc.com/hk/" class="sc-country__country-link" title="Hong Kong">
                                        Hong Kong
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="IND">
                                    <a href="https://www.sc.com/in/" class="sc-country__country-link" title="India">
                                        India
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="IDN">
                                    <a href="https://www.sc.com/id/en/" class="sc-country__country-link" title="Indonesia">
                                        Indonesia
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="IRL">
                                    <a href="https://www.sc.com/ie/" class="sc-country__country-link" title="Ireland">
                                        Ireland
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="ITA">
                                    <a href="https://www.sc.com/it/en/" class="sc-country__country-link" title="Italy">
                                        Italy
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="JPN">
                                    <a href="https://www.sc.com/jp/" class="sc-country__country-link" title="Japan">
                                        Japan
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="JEY">
                                    <a href="https://www.sc.com/je/" class="sc-country__country-link" title="Jersey">
                                        Jersey
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="JOR">
                                    <a href="https://www.sc.com/jo/" class="sc-country__country-link" title="Jordan">
                                        Jordan
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="KEN">
                                    <a href="https://www.sc.com/ke/" class="sc-country__country-link" title="Kenya">
                                        Kenya
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="VTA">
                                    <a href="https://www.sc.com/la/" class="sc-country__country-link" title="Laos">
                                        Laos
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="LBN">
                                    <a href="https://www.sc.com/lb/" class="sc-country__country-link" title="Lebanon">
                                        Lebanon
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="MFM">
                                    <a href="https://www.sc.com/mo/" class="sc-country__country-link" title="Macau">
                                        Macau
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="MYS">
                                    <a href="https://www.sc.com/my/" class="sc-country__country-link" title="Malaysia">
                                        Malaysia
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="MUS">
                                    <a href="https://www.sc.com/mu/" class="sc-country__country-link" title="Mauritius">
                                        Mauritius
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="MEX">
                                    <a href="https://www.sc.com/us/" class="sc-country__country-link" title="Mexico">
                                        Mexico
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="MMR">
                                    <a href="https://www.sc.com/en/contact-us/" class="sc-country__country-link" title="Myanmar">
                                        Myanmar
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="NPL">
                                    <a href="https://www.sc.com/np/" class="sc-country__country-link" title="Nepal">
                                        Nepal
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="NGA">
                                    <a href="https://www.sc.com/ng/" class="sc-country__country-link" title="Nigeria">
                                        Nigeria
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="OMN">
                                    <a href="https://www.sc.com/om-en/" class="sc-country__country-link" title="Oman">
                                        Oman
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="PAK">
                                    <a href="https://www.sc.com/pk/" class="sc-country__country-link" title="Pakistan">
                                        Pakistan
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="PER">
                                    <a href="https://www.sc.com/co-en/" class="sc-country__country-link" title="Peru">
                                        Peru
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="PHL">
                                    <a href="https://www.sc.com/ph/" class="sc-country__country-link" title="Philippines">
                                        Philippines
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="QAT">
                                    <a href="https://www.sc.com/qa/" class="sc-country__country-link" title="Qatar">
                                        Qatar
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="SGP">
                                    <a href="https://www.sc.com/sg/" class="sc-country__country-link" title="Singapore">
                                        Singapore
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="ZAF">
                                    <a href="https://www.sc.com/za/" class="sc-country__country-link" title="South Africa">
                                        South Africa
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="KOR">
                                    <a href="https://www.standardchartered.co.kr/np/kr/Intro.jsp" class="sc-country__country-link" title="South Korea">
                                        South Korea
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="LKA">
                                    <a href="https://www.sc.com/lk/" class="sc-country__country-link" title="Sri Lanka">
                                        Sri Lanka
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="SWE">
                                    <a href="https://www.sc.com/se/" class="sc-country__country-link" title="Sweden">
                                        Sweden
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="TWN">
                                    <a href="https://www.sc.com/tw/" class="sc-country__country-link" title="Taiwan">
                                        Taiwan
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="TZA">
                                    <a href="https://www.sc.com/tz/" class="sc-country__country-link" title="Tanzania">
                                        Tanzania
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="THA">
                                    <a href="https://www.sc.com/th-en/" class="sc-country__country-link" title="Thailand">
                                        Thailand
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="GMB">
                                    <a href="https://www.sc.com/gm/" class="sc-country__country-link" title="The Gambia">
                                        The Gambia
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="TUR">
                                    <a href="https://www.sc.com/tr-en/" class="sc-country__country-link" title="Turkey">
                                        Turkey
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="UGA">
                                    <a href="https://www.sc.com/ug/" class="sc-country__country-link" title="Uganda">
                                        Uganda
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="ARE">
                                    <a href="https://www.sc.com/ae/" class="sc-country__country-link" title="United Arab Emirates">
                                        United Arab Emirates
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="GBR">
                                    <a href="https://www.sc.com/uk/" class="sc-country__country-link" title="United Kingdom">
                                        United Kingdom
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="USA">
                                    <a href="https://www.sc.com/us/" class="sc-country__country-link" title="United States">
                                        United States
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="SGN">
                                    <a href="https://www.sc.com/vn/en/" class="sc-country__country-link" title="Vietnam">
                                        Vietnam
                                    </a>
                                </li>
                                <li class="sc-country__list-item" data-value="ZMB">
                                    <a href="https://www.sc.com/zm/" class="sc-country__country-link" title="Zambia">
                                        Zambia
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="sc-modal__close">
                    <button class="sc-modal__close-button" aria-label="Close country selector"></button>
                </div>
            </div>
        </div>
    </div>
</header>

<div class="m-text-content" data-modal-id="external-links-disclaimer">
    <div class="m-disclaimer">
        <div class="content-wrapper">
            <div class="header">
                <h2 class="title">You're about to leave our website</h2>
            </div>
            <input type="checkbox" checked="checked" class="read-more-state" id="disclaimer-external-links">
            <div class="content">
                <div class="content-mask">
                    <p>This hyperlink will bring to you to another website on the Internet, which is published and
                        operated by a third party which is not owned, controlled or affiliated with or in any way
                        related to Standard Chartered Bank (Hong Kong) Limited or any member of Standard Chartered Group
                        ( the "Bank").</p>
                    <p>The hyperlink is provided for your convenience and presented for information purposes only. The
                        provision of the hyperlink does not constitute endorsement, recommendation, approval, warranty
                        or representation, express or implied, by the Bank of any third party or the hypertext link,
                        product, service or information contained or available therein.</p>
                    <p>The Bank does not have any control (editorial or otherwise) over the linked third party website
                        and is not in any way responsible for the contents available therein. You use or follow this
                        link at your own risk. To the extent permissible by law, the Bank shall not be responsible for
                        any damage or losses incurred or suffered by you arising out of or in connection with your use
                        of the link.</p>
                    <p>Please be mindful that when you click on the link and open a new window in your browser, you will
                        be subject to the terms of use and privacy policies of the third party website that you are
                        going to visit.</p>
                    <br>
                </div>
                <a class="c-button-small is-theme-solid-green-hollow-white is-external-link-button" target="_blank" data-send="close-modal" title="Proceed" data-context="Modal Disclaimer External Links Proceed Button" rel="noopener noreferrer">Proceed to third party website</a>
            </div>
        </div>
    </div>
</div>
<style>
    body>header>div.sc-nav__wrapper>nav>ul>li>div>div>div>div>div>div>ul>li>div>a,
    body>header>div.sc-nav__wrapper>nav>ul>li>div>div>div>div>div>div>ul>li>div>div>a,
    body>header>div.sc-nav__wrapper>nav>ul>li>div>div>div>div>div>div>ul>li>div>a>p.sc-nav-drop__link {
        text-transform: capitalize;
        letter-spacing: 0.2px;
        font-size: 12px;
    }

    #m-aver {
        text-transform: none;
    }

    @media (max-width: 480px) {
        .tailor-img {
            width: 100%;
            height: auto;
        }
    }

    @media(max-width:1023px) {
        .only-desktop-li {
            padding: 0px;
        }
    }

    @media(max-width:1023px) {
        .only-desktop-div {
            display: none
        }
    }
</style>
<style>
	.sc-nav__menu {
        font-family: "SC Sans Web", "SC Prosper Sans Variable", "SC Sans", Arial, sans-serif;
        font-size: 17px;
        padding: 8px 15px;
    }

    .sc-nav__top-in~.sc-nav__top-in .sc-nav__top-btn {
        font-family: "SC Sans Web", "SC Prosper Sans Variable", "SC Sans", Arial, sans-serif;
    }

    .sc-nav__country-btn, .sc-nav__top-btn{
        font-family: "SC Sans Web", "SC Prosper Sans Variable", "SC Sans",Arial,sans-serif;
    }
    @media (min-width:1024px) {

        #sc-nav-drop__col_2::before,
        #sc-nav-drop__col_3::before {
            content: '';
            width: 1px;
            height: 90%;
            background: #e1e1e1;
            position: absolute;
            left: 0;
            top: 5%;
        }
		.sc-nav__login--full .sc-login-drop .sc-nav__login-lists-box-title {
       height: auto;
}
    }

    @media (max-width:1023px) {
        #sc-nav-drop__col-item-1 {
            margin-bottom: 0px;
        }
    }
	@media (max-width:1023px){
	.sc-nav .only-mobile-login {
		display: -webkit-box;
		display: -ms-flexbox;
		display: flex
	}

	.sc-nav .only-desktop-login {
		display: none
	}
}
@media (min-width: 1024px){
    .sc-nav .only-mobile-login {
        display: none
    }

    .sc-nav .only-desktop-login {
        display: -webkit-inline-box;
        display: -ms-inline-flexbox;
        display: block
    }
	.top-navigation .sc-nav-drop__col-promo {
		min-width: 311px !important;
	}

}

#sc_nav_clients{
	border-color:#e1e1e1;
}


#sc_nav_clients:hover{
	color:#000 !important;
	border-color:#e1e1e1;
	background:#fff;
}

.sc-nav__login-lists-box:hover{
	color:#000 !important;
}

#sc_nav_clients_title{
	color:#000;
	height:auto;
	margin: 0 0 16px;
	font-size: 16px;
	font-weight: 400;
	padding: 0;
    border: 0;
}

.sc_nav_channel_button{
	border: 1px solid rgb(85, 85, 85);
}

.sc_nav_channel_button:hover{
	border: 1px solid #2772c7;
}

#sc_nav_channel_button_a{
	color:rgb(85, 85, 85);
	text-transform:initial;
}

.sc_nav_channel_button:hover #sc_nav_channel_button_a{
	color:#2772c7;
}	
</style>
<script type="text/javascript">
    document.getElementById("sc_nav_channel_button_1").onclick = function () {
        location.href = "https://www.sc.com/hk/ibk-redirect/";
    };
	document.getElementById("sc_nav_channel_button_2").onclick = function () {
        location.href = "https://wealth.sc.com/wm/full/hk/oe/desktop/#!/login?lang=en_HK";
    };
	document.getElementById("sc_nav_channel_button_3").onclick = function () {
        location.href = "https://s2b.standardchartered.com/unifiedlogin/login/index.html?utm_source=sc.com-hk-en&utm_medium=login-widget-menu-item&utm_campaign=sc-retail-traffic";
    };
	document.getElementById("sc_nav_channel_button_4").onclick = function () {
        location.href = "https://www.sc.com/hk/promotions/credit-cards/new-reward-redemption/";
    };
</script><link rel="stylesheet" id="sc-banners-styles-css" href="https://av.sc.com/assets/global/css/sc-banners.min.css?ver=b0b95ac" media="all">


<div class="sc-bnr web-three-one sc-bnr-is-cvp sc-bnr-product-variation" id="sc-lb-module-masthead-cvp" data-post-status="publish-status" data-post-status-label="Published">
		<div class="sc-bnr__bg-wrapper">
					<picture>
														<source srcset="https://av.sc.com/hk/content/images/hk-pil-summer-campaign-wave-carousel-1600-490.png" media="(min-width: 768px)">
														<source srcset="https://av.sc.com/hk/content/images/hk-pil-summer-campaign-wave-carousel-768-350.jpg" media="(max-width: 767px)">
								<img src="https://av.sc.com/hk/content/images/hk-pil-summer-campaign-wave-carousel-1600-490.png" class="sc-bnr-image" loading="lazy" alt="Hk pil summer campaign wave carousel ">
			</picture>
				</div>
	<div class="sc-bnr__wrapper">
		<div class="sc-bnr__calculator-wrapper">
						<div class="sc-bnr__content sc-bnr__content--bg-transparent">
				<div class="sc-bnr__box">
																							<h1 class="sc-bnr-title">Take the first step toward your dreams with extra cash flow and interest as low as HKD10 from Personal Loan</h1>
																						<p class="sc-bnr-desc">Need extra funds to achieve your goals? We have you covered! Apply for a Personal Instalment Loan with daily interest as low as HKD10 today.</p>
																<div class="sc-bnr-cvp">
																							<div class="sc-bnr-cvp__col">
																			<p class="sc-bnr-cvp__title">Daily Interest as low </p>
																												<p class="sc-bnr-cvp__main">as <strong>HKD 10^</strong></p>
																										</div>
																							<div class="sc-bnr-cvp__col">
																			<p class="sc-bnr-cvp__title">Handling Fee </p>
																												<p class="sc-bnr-cvp__main"><strong>0%</strong></p>
																										</div>
																					</div>
																											<ul class="sc-bnr-buttons sc-bnr-buttons--block">
																								<li>
					<a href="https://origination.sc.com/onboarding/hk/apply.html?product=1258&amp;campaign=HKPIL23PLSTP10&amp;premium=1258&amp;cardType=3268&amp;affiliation=2132&amp;lang=en" title="Apply Now" data-context="Masthead CTA" class="c-button sc-btn" target="_blank" rel="noopener noreferrer" data-widget-name="masthead">
			<span class="only-desktop">Apply Now</span>
							<span class="only-mobile">Apply Now</span>
					</a>
	</li>
																																<li>
					<a href="https://av.sc.com/hk/content/docs/hk-kfs-personal-instalment-loan.pdf" title="Key Facts Statement" data-context="Masthead CTA" class="c-button sc-btn-arrow" target="_blank" rel="noopener noreferrer">
			<span class="only-desktop">Key Facts Statement</span>
							<span class="only-mobile">Key Facts Statement</span>
					</a>
	</li>
																												</ul>
									</div>
			</div>
					</div>
	</div>
</div>
<link rel="stylesheet" id="sc-hk-interest-calculator-style-css" href="https://av.sc.com/assets/global/css/sc-interest-calculator.min.css?ver=b0b95ac" media="all">
<link rel="stylesheet" id="sc-hk-pil-calculator-style-css" href="https://av.sc.com/assets/global/css/sc-hk-pil-calculator.min.css?ver=b0b95ac" media="all">
<div class="sc-pil-calculator-variant">
<div class="sc-pil-calculator sc-pil-calculator-hk sc-common-calculator-class" rate-details="[{&quot;aprRate&quot;:[{&quot;loanAmountMin&quot;:5000,&quot;loanAmountMax&quot;:200000,&quot;rate&quot;:{&quot;12&quot;:0.31,&quot;24&quot;:0.31,&quot;36&quot;:0.31,&quot;48&quot;:0.312,&quot;60&quot;:0.315},&quot;apr&quot;:{&quot;12&quot;:7.01,&quot;24&quot;:7.22,&quot;36&quot;:7.23,&quot;48&quot;:7.25,&quot;60&quot;:7.26}},{&quot;loanAmountMin&quot;:200000,&quot;loanAmountMax&quot;:500000,&quot;rate&quot;:{&quot;12&quot;:0.27,&quot;24&quot;:0.27,&quot;36&quot;:0.27,&quot;48&quot;:0.271,&quot;60&quot;:0.273},&quot;apr&quot;:{&quot;12&quot;:6.09,&quot;24&quot;:6.28,&quot;36&quot;:6.3,&quot;48&quot;:6.3,&quot;60&quot;:6.31}},{&quot;loanAmountMin&quot;:500000,&quot;loanAmountMax&quot;:700000,&quot;rate&quot;:{&quot;12&quot;:0.23,&quot;24&quot;:0.23,&quot;36&quot;:0.231,&quot;48&quot;:0.232,&quot;60&quot;:0.233},&quot;apr&quot;:{&quot;12&quot;:5.18,&quot;24&quot;:5.34,&quot;36&quot;:5.39,&quot;48&quot;:5.4,&quot;60&quot;:5.4}},{&quot;loanAmountMin&quot;:700000,&quot;loanAmountMax&quot;:1500000,&quot;rate&quot;:{&quot;12&quot;:0.23,&quot;24&quot;:0.23,&quot;36&quot;:0.23,&quot;48&quot;:0.231,&quot;60&quot;:0.232},&quot;apr&quot;:{&quot;12&quot;:5.18,&quot;24&quot;:5.34,&quot;36&quot;:5.37,&quot;48&quot;:5.38,&quot;60&quot;:5.38}},{&quot;loanAmountMin&quot;:1500000,&quot;loanAmountMax&quot;:-1,&quot;rate&quot;:{&quot;12&quot;:0.083,&quot;24&quot;:0.22,&quot;36&quot;:0.22,&quot;48&quot;:0.22,&quot;60&quot;:0.221},&quot;apr&quot;:{&quot;12&quot;:1.85,&quot;24&quot;:5.11,&quot;36&quot;:5.13,&quot;48&quot;:5.13,&quot;60&quot;:5.13}}],&quot;tenorValues&quot;:[12,24,36,48,60]}]" data-currency-code="HKD" data-comma-format="3" data-interest-type="monthly" id="sc-lb-module-hk-pil-calculator" data-post-status="publish-status" data-post-status-label="Published">
	<div class="sc-pil-calculator__box">
					<h2 class="sc-pil-calculator__title">Personal Instalment Loan Calculator</h2>
							<div class="sc-pil-calculator__slider-main">
				<div class="sc-pil-calculator__row">
																<div class="sc-pil-calculator__discription">Loan Amount</div>
										<div class="sc-pil-calculator__input-box">
													<div class="sc-pil-calculator__input-text">HKD</div>
												<input type="text" class="sc-pil-calculator__input sc-pil-calculator__input--amount-value" value="20000" aria-label="Loan Amount" name="loanamount" tabindex="-1">
					</div>
				</div>
				<div class="sc-pil-calculator__slider">
					<div class="sc-range-slider sc-pil-calculator__input--amount noUi-target noUi-ltr noUi-horizontal noUi-txt-dir-ltr" data-max="4000000" data-min="5000" data-default="20000" data-step="1000" aria-label="Drage here to move slider"><div class="noUi-base"><div class="noUi-connects"><div class="noUi-connect" style="transform: translate(0%, 0px) scale(0.00375469, 1);"></div></div><div class="noUi-origin" style="transform: translate(-99.6245%, 0px); z-index: 4;"><div class="noUi-handle noUi-handle-lower" data-handle="0" tabindex="0" role="slider" aria-orientation="horizontal" aria-valuemin="5000.0" aria-valuemax="4000000.0" aria-valuenow="20000.0" aria-valuetext="20000.00"><div class="noUi-touch-area"></div></div></div></div></div>
				</div>
									<div class="sc-pil-calculator__prompt-msg sc-pil-calculator__prompt-msg--mt">Please enter a valid amount</div>
							</div>
							<div class="sc-pil-calculator__slider-main">
				<div class="sc-pil-calculator__row">
																<div class="sc-pil-calculator__discription">
							Loan Period						</div>
										<div class="sc-pil-calculator__input-box sc-pil-calculator__input-box--mod">
						<select class="sc-pil-calculator__input sc-pil-calculator__slider-tenor-value" aria-label="Loan Period" name="tenor">
															<option value="" disabled="">Select</option>
																													<option value="12" selected="">12 month(s)</option>
															<option value="24">24 month(s)</option>
															<option value="36">36 month(s)</option>
															<option value="48">48 month(s)</option>
															<option value="60">60 month(s)</option>
													</select>
					</div>
				</div>
				<div class="sc-pil-calculator__slider">
					<div class="sc-range-slider sc-pil-calculator__slider-tenor noUi-target noUi-ltr noUi-horizontal noUi-txt-dir-ltr" data-max="60" data-min="12" data-default="12" data-step="12" snap="true" aria-label="Drage here to move slider">
					<div class="noUi-base"><div class="noUi-connects"><div class="noUi-connect" style="transform: translate(0%, 0px) scale(0, 1);"></div></div><div class="noUi-origin" style="transform: translate(-100%, 0px); z-index: 4;"><div class="noUi-handle noUi-handle-lower" data-handle="0" tabindex="0" role="slider" aria-orientation="horizontal" aria-valuemin="12.0" aria-valuemax="60.0" aria-valuenow="12.0" aria-valuetext="12.00"><div class="noUi-touch-area"></div></div></div></div></div>
				</div>
									<div class="sc-pil-calculator__prompt-msg sc-pil-calculator__prompt-msg--mt">Please select a valid tenor</div>
							</div>
			</div>
	<div class="sc-pil-calculator__result">
					<div class="sc-pil-calculator__result-row">
				<div class="sc-pil-calculator__result-discription">
					<div class="col label">Annualised Percentage Rate as low as</div>
				</div>
				<div class="sc-pil-calculator__result-value sc-pil-calculator__apr">7.01%</div>
			</div>
							<div class="sc-pil-calculator__result-row">
				<div class="sc-pil-calculator__result-discription">
					<div class="col label">Monthly Repayment as low as</div>
				</div>
				<div class="sc-pil-calculator__result-value sc-pil-calculator__payment">HKD 1,728.67</div>
			</div>
							<div class="sc-pil-calculator__note">Note: Monthly Repayment and Annualised Percentage Rate displayed here are for reference only and are subject to credit approval</div>
							<ul class="sc-bnr-buttons">
															<li>
					<a href="https://origination.sc.com/onboarding/hk/apply.html?product=1258&amp;campaign=HKPIL23PLSTP10&amp;premium=1258&amp;cardType=3268&amp;affiliation=2132&amp;lang=en" title="Apply Now" data-context="Calculator CTA" class="c-button sc-btn" target="_blank" rel="noopener noreferrer" data-widget-name="calculator">
			<span class="only-desktop">Apply Now</span>
							<span class="only-mobile">Apply Now</span>
					</a>
	</li>
																				<li class="sc-only-mobile">
					<a href="https://av.sc.com/hk/content/docs/hk-kfs-personal-instalment-loan.pdf" title="Key Facts Statement" data-context="Calculator CTA" class="c-button sc-btn-arrow" target="_blank" rel="noopener noreferrer">
			<span class="only-desktop">Key Facts Statement</span>
							<span class="only-mobile">Key Facts Statement</span>
					</a>
	</li>
												</ul>
			</div>
</div>
</div>
<script type="application/ld+json">
    [
    {
        "@context": "https://schema.org",
    "@type": "LoanOrCredit",
    "name": "Personal Instalment Loan",
    "url": "https://www.sc.com/hk/loans/personal-instalment-loan/",
    "description": "Borrowing money in Hong Kong with SC Personal Instalment Loan. Receives up to HKD4 million/18x your monthly salary with an interest rate as low as 1.85%.",
    "image": "https://av.sc.com/hk/content/images/hk-loans-pil-summer-campaign-banner-jul24-1600-490.jpg",
    "loanType": "Personal Loan",
    "feesAndCommissionsSpecification": "https://av.sc.com/hk/content/docs/hk-kfs-personal-instalment-loan.pdf",
    "interestRate": "1.85",
    "amount": {
        "@type": "MonetaryAmount",
    "minValue": "5000",
    "maxValue": "4000000",
    "currency": "HKD"
  },
    "annualPercentageRate": {
        "@type": "QuantitativeValue",
    "name": "Effective Interest Rate",
    "minValue": "1.85",
    "maxValue": "7.25"
  },
    "loanTerm": {
        "@type": "QuantitativeValue",
    "unitCode": "ANN",
    "minValue": "1",
    "maxValue": "5"
  },
    "offers": {
        "@type": "Offer",
    "offeredBy": {
        "@type": "BankOrCreditUnion",
    "name": "Standard Chartered Hong Kong",
    "id": "https://www.sc.com/hk/"
    },
    "description": "Standard Chartered Hong Kong offers personal and business banking services: bank accounts, credit cards, loans, mortgages, investments, MPF and insurance."
  }
},
    {
        "@context": "https://schema.org",
    "@type": "ContactPoint",
    "telephone": "852-3408-1628",
    "contactType": "Customer Service",
    "areaServed": "HK",
    "availableLanguage": "English"
},
    {
        "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Standard Chartered Bank Hongkong",
    "url": "https://www.sc.com/hk/",
    "logo": "https://av.sc.com/assets/global/images/components/header/standard-chartered-logo.svg",
    "contactPoint": [{
        "@type": "ContactPoint",
    "telephone": "852-3408-1628",
    "contactType": "Customer Service"
  }],
    "sameAs": "https://www.facebook.com/standardcharteredhk/"
},
    {
        "@context": "https://schema.org",
    "@type": "Action",
    "name": "Apply for a Personal Instalment Loan",
    "target": "https://www.sc.com/hk/loans/personal-instalment-loan/",
    "actionStatus": "PotentialActionStatus"
}
    ]
</script><link rel="stylesheet" id="sc-product-action-style-css" href="https://av.sc.com/assets/global/css/product-actions.min.css?ver=b0b95ac" media="all">

<div class="sc-product-actions" id="sc-lb-module-product-action" data-post-status="publish-status" data-post-status-label="Published">
	<div class="sc-product-actions__content-wrapper">
		<div class="sc-product-actions__col sc-product-actions__col-image">
			<img width="560" height="280" src="https://av.sc.com/hk/content/images/hk-loans-pil-dc-xsell-560-280.png" class="sc-product-actions__bg-img" alt="Hk loans pil dc xsell " loading="lazy" decoding="async">		</div>
		<div class="sc-product-actions__col sc-product-actions__col-content">
										<div class="sc-product-actions__desc-short">
					Double benefits of up to HKD9,500 Cash Rebates with Bonus Payroll Account and Personal Loans				</div>
										<div class="sc-product-actions__desc-long">
					<ul class="sc-product-actions__lister">
 	<li class="sc-product-actions__list c-icon icon-tick">Enjoy up to HKD8,000 Cash Rebates when you apply for a Personal Instalment Loan</li>
 	<li class="sc-product-actions__list c-icon icon-tick">Online Welcome Offer of up to HKD1,500 Cash Rebates</li>
 	<li class="sc-product-actions__list c-icon icon-tick">Consolidate your payday and repayment date for effortless financial planning</li>
</ul>				</div>
										<ul class="sc-product-actions__buttons">
					<li>
					<a href="https://origination.sc.com/onboarding/hk/apply.html?product=1258&amp;campaign=HKPIL23PLSTP10&amp;premium=1258&amp;cardType=3268&amp;affiliation=2132&amp;lang=en" title="Apply Now" data-context="" class="c-button c-button is-theme-solid-green" target="_blank" rel="noopener noreferrer" data-widget-name="na">
			<span class="only-desktop">Apply Now</span>
							<span class="only-mobile">Apply Now</span>
					</a>
	</li>
				</ul>
								</div>
	</div>
</div>
<div class="m-centered-text" id="sc-lb-module-product-description" data-post-status="publish-status" data-post-status-label="Published">
	<div class="content">
					<h2 class="title">Realise your goals with SC Personal Loan</h2>
							<p class="message">Apply for a Personal Instalment Loan with daily interest as low as HKD10 today.</p>
					</div>
</div>
<link rel="stylesheet" id="sc-hk-product-feature-style-css" href="https://av.sc.com/assets/global/css/product-key-features.min.css?ver=b0b95ac" media="all">



<div class="m-sticky-column-box">

						
				
					<div class="section sticky-section" data-bg-color="#ebf2f7" data-text-color="#007eb2">

					<div class="left-col sticky-col blue" pin-element="true" pin-start-pos="1809.78125" pin-end-pos="2495.59325" pin-offset-pos="685.812" pin-width="281.594">
						<div class="sticky-inner blue" style="position: relative; top: 0px; width: 100%;">
															<h2>SC Personal Instalment Loan Key Product Features:</h2>
													</div>
					</div>

				
				<div class="right-col">
						<div class="col-section">
		<div>
						<div class="flex">
				<div class="col">
											<p class="pre-highlight blue">
							Basic Cash Back and New Client Cash Back – Up to						</p>
																				<div class="highlight-number blue" style="">
													<span class="highlight-label">
								HKD							</span>
												8,000											</div>
																			</div>
							</div>
		</div>
							</div>
			<div class="col-section">
		<div>
						<div class="flex">
				<div class="col">
											<p class="pre-highlight blue">
							Annualised Percentage Rate as low as						</p>
																				<div class="highlight-number blue" style="">
												1.85<span class="highlight-label">%</span><sup>#</sup>											</div>
																			</div>
									<div class="col">
													<p class="pre-highlight green">Daily loan interest as low as</p>
																								<div class="highlight-number green " style="">
															<span class="highlight-label">
									HKD								</span>
														10<sup>^</sup>													</div>
																							</div>
							</div>
		</div>
							</div>
			<div class="col-section">
		<div>
						<div class="flex">
				<div class="col">
											<p class="pre-highlight blue">
							Handling fee						</p>
																				<div class="highlight-number blue" style="">
												0%											</div>
																			</div>
									<div class="col">
													<p class="pre-highlight green">Loan amount up to</p>
												<div>												<div class="highlight-number green " style="display: inline;">
														18X													</div>
																			<span class="highlight-remarks"> monthly salary or HKD4,000,000 (whichever is lower)</span>
												</div>					</div>
							</div>
		</div>
							</div>
			<div class="col-section">
		<div>
						<div class="flex">
				<div class="col">
											<p class="pre-highlight blue">
							Loan tenor up to						</p>
																				<div class="highlight-number blue" style="">
												60<span class="highlight-label">months</span>											</div>
																			</div>
							</div>
		</div>
							</div>
		
									</div>
			</div>

		
				
					<div class="section sticky-section" data-bg-color="#e9f4e7" data-text-color="#42ad59">
					<div class="left-col sticky-col green" pin-element="true" pin-start-pos="2684.78125" pin-end-pos="2833.96825" pin-offset-pos="149.187" pin-width="281.594">
						<div class="sticky-inner green" style="position: relative; top: 0px; width: 100%;">
																							<h3 class="sticky-section-head">Other Product Features:</h3>													</div>
					</div>

				
				<div class="right-col">
					
										<div class="col-section">
						<ul class="checked-list w-list-unstyled">
														<li class="checked-list-item">7-Day Cooling-off Period: Early bank loan redemption fees and charges waiver</li>
							
														<li class="checked-list-item">Preliminary Approval in 5 Minutes: Online personal loan application screened in 5 minutes upon submission</li>
							
														<li class="checked-list-item">Top-up Service for Existing Personal Instalment Loan Clients: SC Personal Instalment Loan offers a top-up service allowing existing customers to obtain extra funds easily. Borrow extra money or extend the loan on top of an existing personal loan to meet urgent financial needs.</li>
							
							
													</ul>

											</div>
									</div>
			</div>

		
				
					<div class="section sticky-section" data-bg-color="#e9f4e7" data-text-color="#42ad59">
					<div class="left-col sticky-col green" pin-element="true" pin-start-pos="2953.5625" pin-end-pos="2968.7655" pin-offset-pos="15.203000000000003" pin-width="281.594">
						<div class="sticky-inner green" style="position: relative; top: 0px; width: 100%;">
																							<h3 class="sticky-section-head">Personal Loan Calculator for Repayment</h3>													</div>
					</div>

				
				<div class="right-col">
					
										<div class="col-section">
						<ul class="checked-list w-list-unstyled">
														<li class="checked-list-item">Quickly estimate your monthly repayment amount, loan APR, flat rate, and monthly interest with our Personal Loan Calculator</li>
							
							
							
							
													</ul>

														<ul class="buttons align-center">
					<a href="https://www.sc.com/hk/loans/personal-instalment-loan-repayment-calculator/" class="learn-more-button en w-inline-block" target="_blank" rel="noopener noreferrer">Personal Loan Repayment Calculator</a>
			
	</ul>
	<div class="learn-more-content">
					</div>
													</div>
									</div>
			</div>

			</div>
<div class="m-tables" id="sc-lb-module-fee-and-rate-1" data-post-status="publish-status" data-post-status-label="Published">
	<div class="content-wrapper">
									<div class="content" id="table-content-858452-1">
																			</div>
					<div class="content" id="table-content-858452-2">
									<div class="sub-content">
																			<div class="description"><p>Remarks</p>
<p>^ Daily loan interest as low as HK$10 (rounded down to the nearest integer) is calculated with the loan amount of HK$100,000, tenor of 12 months and monthly flat rate of 0.31% which is equivalent to APR of 7.01%.&nbsp; (Loan amount: $100,000 * monthly flat rate 0.31% * Tenor 12 months) &nbsp;/ 365&nbsp;&nbsp;days = HK$10.19</p>
<p>* Save total interest expense up to 15%: Assuming the customer is a new customer with a loan amount of HK$1,500,000, tenor of 36 months, annualised percentage rate of 5.13% and the total interest is HK$118,800 = HK$1,500,000 (loan amount) * 0.22% (monthly flat rate) *36 months (tenor). The total cash rebate amount is HK$18,000. which is equivalent to 15% of the total interest expense (HK$18,000/HK$118,800). New Clients are applicants who are not holding any loans and/or credit cards issued by the Bank at the time of this loan application</p>
<p># The Annualised Percentage Rate is 1.85% (for clients with loan amount of HKD$1,500,000 or above and tenor of 12 months). APRs are reference rates which include the basic loan interest rate and other applicable fees and charges of a product expressed as an annualised rate. This APR does not include cash rebate. The preferential interest rates are only applicable to clients who are not holding any Standard Chartered Credit Cards/Personal Loan at the time of this application. The Bank reserves the right to determine the applicable loan interest rate and handling fee, and to approve a person instalment loan application, which is to be considered on a case-by-case basis in accordance with the client’s credit records and other relevant factors as the Bank may consider in its absolute discretion. All offers are subject to Terms and Conditions</p>
<p>1. The Monthly Flat Rate shown above was for reference only.</p>
<p>2. For every HKD1,000 loan amount.</p>
<p>3. The above Annualised Percentage Rates (“APR”) are reference rates which include the basic interest rate and other fees and charges of a product expressed as an annualised rate (if applicable). This APR does not include cash rebate.</p>
<p>The Annualised Percentage Rate ranged from 1.85% to 36% and flexible repayment period of 12 to 60 months. An APR is a reference rate which includes the basic loan interest rate and other applicable fees and charges of a product expressed as an annualised rate. This APR does not include cash rebate. The Bank reserves the right to determine the applicable interest rate and handling fee and acceptance of a loan application, which is to be considered on a case-by-case basis in accordance with the client’s credit records and other relevant factors.</p>
<p>The operating hours of our Loan Application Hotline are from Monday to Friday: 10am – 7pm.</p>
</div>
											</div>
																			</div>
							</div>
</div>
<div class="m-tables" id="sc-lb-module-repayment-table" data-post-status="publish-status" data-post-status-label="Published">
	<input type="hidden" value="" id="full_view_rt" class="full_view_rt">
	<div class="content-wrapper frt">
			<div class="header">

									<h3 class="title">SC Personal Instalment Loan Repayment Table</h3>
				
							</div>

		<div class="content">
			<div class="table-wrapper frt-primary-container" style="display: block;">
				<table><thead>
						<tr>
							<th width="150"><div class="th-wrapper"><p>Loan Amount^ (HKD)</p>
</div></th>
							<th>
																<select class="frt-primary-selector fr-select">
																																									<option value="repayment-loan-table-1">
												<p>$5,000 – $199,999</p>
											</option>
																																																			<option value="repayment-loan-table-2">
												<p>$200,000 – $499,999</p>
											</option>
																																																			<option value="repayment-loan-table-3">
												<p>$500,000 – $699,999</p>
											</option>
																																																			<option value="repayment-loan-table-4">
												<p>$700,000 – $1,499,999</p>
											</option>
																																																			<option value="repayment-loan-table-5">
												<p>$1,500,000 – or above</p>
											</option>
																											</select>
							</th>
						</tr>
					</thead></table>
			</div>

			<div class="table-wrapper frt-secondary-container">
				<table><thead style="">
						<tr>
							<th width="150"><div class="th-wrapper"><p>LOAN RANGE</p>
</div></th>
							<th>
								<select class="frt-secondary-selector fr-select"><option value="2">12 months</option><option value="3">24 months</option><option value="4">36 months</option><option value="5">48 months</option><option value="6">60 months</option></select>
							</th>
						</tr>
					</thead></table>
			</div>
		</div>

		<!-- Responsive table - starts -->
					<div class="content frt-box" id="repayment-loan-table-1" style="display: block;">
								<!-- Non Mobile view - starts -->
				<div class="table-wrapper is-not-mobile-table">
										<table><thead>
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper"><p>12 months</p>
</div></th>
																<th><div class="th-wrapper"><p>24 months</p>
</div></th>
																<th><div class="th-wrapper"><p>36 months</p>
</div></th>
																<th><div class="th-wrapper"><p>48 months</p>
</div></th>
																<th><div class="th-wrapper"><p>60 months</p>
</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.31%</p>
</td>
																<td><p>0.31%</p>
</td>
																<td><p>0.31%</p>
</td>
																<td><p>0.312%</p>
</td>
																<td><p>0.315%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$86.43</p>
</td>
																<td><p>$44.77</p>
</td>
																<td><p>$30.88</p>
</td>
																<td><p>$23.95</p>
</td>
																<td><p>$19.82</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>7.01%</p>
</td>
																<td><p>7.22%</p>
</td>
																<td><p>7.23%</p>
</td>
																<td><p>7.25%</p>
</td>
																<td><p>7.26%</p>
</td>
															</tr>
						</tbody></table>
									</div>
				<!-- Non Mobile view - ends -->

				<!-- Mobile view - starts -->
				<div class="table-wrapper is-mobile-table">
					<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper">
																		<p>12 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="3">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="2">◀</span>
																		<p>24 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="4">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="3">◀</span>
																		<p>36 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="5">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="4">◀</span>
																		<p>48 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="6">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="5">◀</span>
																		<p>60 months</p>
																	</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.31%</p>
</td>
																<td><p>0.31%</p>
</td>
																<td><p>0.31%</p>
</td>
																<td><p>0.312%</p>
</td>
																<td><p>0.315%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$86.43</p>
</td>
																<td><p>$44.77</p>
</td>
																<td><p>$30.88</p>
</td>
																<td><p>$23.95</p>
</td>
																<td><p>$19.82</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>7.01%</p>
</td>
																<td><p>7.22%</p>
</td>
																<td><p>7.23%</p>
</td>
																<td><p>7.25%</p>
</td>
																<td><p>7.26%</p>
</td>
															</tr>
						</tbody></table>
				</div>
				<!-- Mobile view - ends -->
			</div>
					<div class="content frt-box" id="repayment-loan-table-2" style="display: none;">
								<!-- Non Mobile view - starts -->
				<div class="table-wrapper is-not-mobile-table">
										<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper"><p>12 months</p>
</div></th>
																<th><div class="th-wrapper"><p>24 months</p>
</div></th>
																<th><div class="th-wrapper"><p>36 months</p>
</div></th>
																<th><div class="th-wrapper"><p>48 months</p>
</div></th>
																<th><div class="th-wrapper"><p>60 months</p>
</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.27%</p>
</td>
																<td><p>0.27%</p>
</td>
																<td><p>0.27%</p>
</td>
																<td><p>0.271%</p>
</td>
																<td><p>0.273%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$86.03</p>
</td>
																<td><p>$44.37</p>
</td>
																<td><p>$30.48</p>
</td>
																<td><p>$23.54</p>
</td>
																<td><p>$19.40</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>6.09%</p>
</td>
																<td><p>6.28%</p>
</td>
																<td><p>6.30%</p>
</td>
																<td><p>6.30%</p>
</td>
																<td><p>6.31%</p>
</td>
															</tr>
						</tbody></table>
									</div>
				<!-- Non Mobile view - ends -->

				<!-- Mobile view - starts -->
				<div class="table-wrapper is-mobile-table">
					<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper">
																		<p>12 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="3">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="2">◀</span>
																		<p>24 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="4">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="3">◀</span>
																		<p>36 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="5">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="4">◀</span>
																		<p>48 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="6">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="5">◀</span>
																		<p>60 months</p>
																	</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.27%</p>
</td>
																<td><p>0.27%</p>
</td>
																<td><p>0.27%</p>
</td>
																<td><p>0.271%</p>
</td>
																<td><p>0.273%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$86.03</p>
</td>
																<td><p>$44.37</p>
</td>
																<td><p>$30.48</p>
</td>
																<td><p>$23.54</p>
</td>
																<td><p>$19.40</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>6.09%</p>
</td>
																<td><p>6.28%</p>
</td>
																<td><p>6.30%</p>
</td>
																<td><p>6.30%</p>
</td>
																<td><p>6.31%</p>
</td>
															</tr>
						</tbody></table>
				</div>
				<!-- Mobile view - ends -->
			</div>
					<div class="content frt-box" id="repayment-loan-table-3" style="display: none;">
								<!-- Non Mobile view - starts -->
				<div class="table-wrapper is-not-mobile-table">
										<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper"><p>12 months</p>
</div></th>
																<th><div class="th-wrapper"><p>24 months</p>
</div></th>
																<th><div class="th-wrapper"><p>36 months</p>
</div></th>
																<th><div class="th-wrapper"><p>48 months</p>
</div></th>
																<th><div class="th-wrapper"><p>60 months</p>
</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.231%</p>
</td>
																<td><p>0.232%</p>
</td>
																<td><p>0.233%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$85.63</p>
</td>
																<td><p>$43.97</p>
</td>
																<td><p>$30.09</p>
</td>
																<td><p>$23.15</p>
</td>
																<td><p>$19</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>5.18%</p>
</td>
																<td><p>5.34%</p>
</td>
																<td><p>5.39%</p>
</td>
																<td><p>5.40%</p>
</td>
																<td><p>5.40%</p>
</td>
															</tr>
						</tbody></table>
									</div>
				<!-- Non Mobile view - ends -->

				<!-- Mobile view - starts -->
				<div class="table-wrapper is-mobile-table">
					<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper">
																		<p>12 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="3">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="2">◀</span>
																		<p>24 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="4">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="3">◀</span>
																		<p>36 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="5">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="4">◀</span>
																		<p>48 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="6">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="5">◀</span>
																		<p>60 months</p>
																	</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.231%</p>
</td>
																<td><p>0.232%</p>
</td>
																<td><p>0.233%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$85.63</p>
</td>
																<td><p>$43.97</p>
</td>
																<td><p>$30.09</p>
</td>
																<td><p>$23.15</p>
</td>
																<td><p>$19</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>5.18%</p>
</td>
																<td><p>5.34%</p>
</td>
																<td><p>5.39%</p>
</td>
																<td><p>5.40%</p>
</td>
																<td><p>5.40%</p>
</td>
															</tr>
						</tbody></table>
				</div>
				<!-- Mobile view - ends -->
			</div>
					<div class="content frt-box" id="repayment-loan-table-4" style="display: none;">
								<!-- Non Mobile view - starts -->
				<div class="table-wrapper is-not-mobile-table">
										<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper"><p>12 months</p>
</div></th>
																<th><div class="th-wrapper"><p>24 months</p>
</div></th>
																<th><div class="th-wrapper"><p>36 months</p>
</div></th>
																<th><div class="th-wrapper"><p>48 months</p>
</div></th>
																<th><div class="th-wrapper"><p>60 months</p>
</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.231%</p>
</td>
																<td><p>0.232%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$85.63</p>
</td>
																<td><p>$43.97</p>
</td>
																<td><p>$30.08</p>
</td>
																<td><p>$23.14</p>
</td>
																<td><p>$18.99</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>5.18%</p>
</td>
																<td><p>5.34%</p>
</td>
																<td><p>5.37%</p>
</td>
																<td><p>5.38%</p>
</td>
																<td><p>5.38%</p>
</td>
															</tr>
						</tbody></table>
									</div>
				<!-- Non Mobile view - ends -->

				<!-- Mobile view - starts -->
				<div class="table-wrapper is-mobile-table">
					<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper">
																		<p>12 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="3">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="2">◀</span>
																		<p>24 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="4">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="3">◀</span>
																		<p>36 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="5">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="4">◀</span>
																		<p>48 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="6">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="5">◀</span>
																		<p>60 months</p>
																	</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.23%</p>
</td>
																<td><p>0.231%</p>
</td>
																<td><p>0.232%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$85.63</p>
</td>
																<td><p>$43.97</p>
</td>
																<td><p>$30.08</p>
</td>
																<td><p>$23.14</p>
</td>
																<td><p>$18.99</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>5.18%</p>
</td>
																<td><p>5.34%</p>
</td>
																<td><p>5.37%</p>
</td>
																<td><p>5.38%</p>
</td>
																<td><p>5.38%</p>
</td>
															</tr>
						</tbody></table>
				</div>
				<!-- Mobile view - ends -->
			</div>
					<div class="content frt-box" id="repayment-loan-table-5" style="display: none;">
								<!-- Non Mobile view - starts -->
				<div class="table-wrapper is-not-mobile-table">
										<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper"><p>12 months</p>
</div></th>
																<th><div class="th-wrapper"><p>24 months</p>
</div></th>
																<th><div class="th-wrapper"><p>36 months</p>
</div></th>
																<th><div class="th-wrapper"><p>48 months</p>
</div></th>
																<th><div class="th-wrapper"><p>60 months</p>
</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.083%</p>
</td>
																<td><p>0.22%</p>
</td>
																<td><p>0.22%</p>
</td>
																<td><p>0.22%</p>
</td>
																<td><p>0.221%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$84.16</p>
</td>
																<td><p>$43.87</p>
</td>
																<td><p>$29.98</p>
</td>
																<td><p>$23.03</p>
</td>
																<td><p>$18.88</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>1.85%</p>
</td>
																<td><p>5.11%</p>
</td>
																<td><p>5.13%</p>
</td>
																<td><p>5.13%</p>
</td>
																<td><p>5.13%</p>
</td>
															</tr>
						</tbody></table>
									</div>
				<!-- Non Mobile view - ends -->

				<!-- Mobile view - starts -->
				<div class="table-wrapper is-mobile-table">
					<table><thead style="">
							<tr>
								<th><div class="th-wrapper"><p>Loan Tenor</p>
</div></th>
																<th><div class="th-wrapper">
																		<p>12 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="3">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="2">◀</span>
																		<p>24 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="4">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="3">◀</span>
																		<p>36 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="5">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="4">◀</span>
																		<p>48 months</p>
																			<span class="right-arrow frt-ss-trigger" data-months="6">▶</span>
																	</div></th>
																<th><div class="th-wrapper">
																			<span class="left-arrow frt-ss-trigger" data-months="5">◀</span>
																		<p>60 months</p>
																	</div></th>
															</tr>
						</thead><tbody>
							<tr>
								<td class="fr-header"><p>Monthly Flat Rate¹</p>
</td>
																<td><p>0.083%</p>
</td>
																<td><p>0.22%</p>
</td>
																<td><p>0.22%</p>
</td>
																<td><p>0.22%</p>
</td>
																<td><p>0.221%</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Monthly Repayment² (HKD)</p>
</td>
																<td><p>$84.16</p>
</td>
																<td><p>$43.87</p>
</td>
																<td><p>$29.98</p>
</td>
																<td><p>$23.03</p>
</td>
																<td><p>$18.88</p>
</td>
															</tr>
							<tr>
								<td class="fr-header"><p>Annualised Percentage Rate³</p>
</td>
																<td><p>1.85%</p>
</td>
																<td><p>5.11%</p>
</td>
																<td><p>5.13%</p>
</td>
																<td><p>5.13%</p>
</td>
																<td><p>5.13%</p>
</td>
															</tr>
						</tbody></table>
				</div>
				<!-- Mobile view - ends -->
			</div>
				<!-- Responsive table - ENDS -->

		<!-- Full Table - starts -->
				<!-- Full Table - ends -->

							<ul class="buttons rt-ctas">
									<li>
					<a href="https://origination.sc.com/onboarding/hk/apply.html?product=1258&amp;campaign=HKP11E2PLWL010&amp;premium=1258&amp;cardType=3268&amp;affiliation=2132&amp;lang=en" title="Apply Now" data-context="" class="c-button is-theme-solid-green-hollow-white" target="_blank" rel="noopener noreferrer" data-widget-name="na">
			<span class="only-desktop">Apply Now</span>
							<span class="only-mobile">Apply Now</span>
					</a>
	</li>
							</ul>
		
	</div>
</div>

<div class="m-eligibility-documents" id="sc-lb-module-eligibility-document" data-post-status="publish-status" data-post-status-label="Published">
	<div class="content-wrapper">
					<div class="header">
				<h3 class="title">Personal Loan Eligibility &amp; Documents</h3>
			</div>
				<div class="content-group">
							<div class="content">
					<h4 class="title">Eligibility</h4>
											<ul class="list">
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-item-8424-1">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">Hong Kong resident aged 20&nbsp;or above</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-item-8424-2">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">Fixed annual income of HKD96,000 or above</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
													</ul>
									</div>
										<div class="content">
					<h4 class="title">Required Documents</h4>
											<ul class="list">
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-document-8424-1">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">Your Hong Kong Permanent Identity Card</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-document-8424-2">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">Your latest residential address proof showing your name</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-document-8424-3">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">For regular income earners, please enclose your latest 1 month’s Bank Statements / Passbook showing your name, account number and salary entries or latest 1 month’s computer generated Payroll Slip, or latest Tax Demand Note</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-document-8424-4">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">For irregular income earners, please enclose your latest 3 month’s Bank Statements / Passbook showing your name, account number and salary entries or latest 3 month’s computer generated Payroll Slip, or latest Tax Demand Note</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-document-8424-5">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">For self-employed applicants, please enclose your Business Registration Certificate AND latest Profits Tax Demand Note</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
															<li class="item" id="sc-lb-module-eligibility-document-eligibility-document-8424-6">
									<div class="item-title">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<div class="text">Note: The bank reserves the rights of requiring more supportive documents for further review.</div>
									</div>
									<div class="item-info">
																			</div>
								</li>
													</ul>
									</div>
					</div>
	</div>
</div>

<div class="m-faqs" id="sc-lb-module-faq" data-post-status="publish-status" data-post-status-label="Published">
	<div class="content-wrapper">
					<div class="header">
				<h3 class="title">Quick and Easy Tips for Personal Instalment Loan</h3>
			</div>
							<input type="checkbox" class="read-more-state" id="faq-more-state-873859">
				<div class="content">

			<ul class="list">
															<li class="item">
							<input id="sc-lb-module-faq-item-873859-0" name="sc-lb-module-faq-item-accordion" type="checkbox">
							<label for="sc-lb-module-faq-item-873859-0" class="item-wrapper">
								<span class="question">
									<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
									<span class="question-text">How to determine the personal loan amount and loan repayment period?</span>
									<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
								</span>
							</label>
							<div class="answer">
								<ul>
<li>When applying for a personal loan, it is crucial to evaluate personal repayment capacity objectively. Ideally, you should only borrow the amount of money you truly need, in order to avoid excessive borrowing.</li>
<li>While calculating the cost of borrowing personal loan, it’s important to include any administrative fee, handling fee and other additional costs associated with personal loan SC Personal Instalment Loan is a bank loan that is free of handling fee, reducing your borrowing costs.</li>
<li>You may also utilize our <a href="https://sc.com/hk/loans/personal-instalment-loan-repayment-calculator/">Standard Chartered’s Personal Instalment Loan Repayment Calculator</a> to quickly estimate your monthly repayment amount as a reference for your financial planning and budgeting for your personal loan.</li>
</ul>
							</div>
						</li>
																				<li class="item">
							<input id="sc-lb-module-faq-item-873859-1" name="sc-lb-module-faq-item-accordion" type="checkbox">
							<label for="sc-lb-module-faq-item-873859-1" class="item-wrapper">
								<span class="question">
									<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
									<span class="question-text">What are the eligibility criteria for applying for a personal loan?</span>
									<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
								</span>
							</label>
							<div class="answer">
								<ul>
<li>It is not difficult to be eligible for a Personal Loan. For instance, for SC Personal Instalment Loan, Hong Kong residents aged 20 or above with a fixed annual income of HKD96,000 or above are eligible to apply.</li>
</ul>
							</div>
						</li>
																				<li class="item">
							<input id="sc-lb-module-faq-item-873859-2" name="sc-lb-module-faq-item-accordion" type="checkbox">
							<label for="sc-lb-module-faq-item-873859-2" class="item-wrapper">
								<span class="question">
									<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
									<span class="question-text">Can I make an early repayment for my personal loan?</span>
									<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
								</span>
							</label>
							<div class="answer">
								<ul>
<li>You have the flexibility to repay the personal loan In additional to the personal loan instalment amount, you must settle all accrued but unpaid loan interest up to the actual settlement date, an early settlement fee of 2.5% of the outstanding balance and any other sum due to us. If the personal loan repayment is made within the 7-Day Cooling-off Period, early redemption fees would be waived. Please note that the bank reserves the right to request the full refund of any cash rebate received during the application or deduct the equivalent value of the cash rebate from any account of the eligible customer.</li>
<li>If you plan to repay the personal loan in full early, you must notify us in writing ten business days before your proposed repayment date.</li>
</ul>
							</div>
						</li>
																				<li class="item">
							<input id="sc-lb-module-faq-item-873859-3" name="sc-lb-module-faq-item-accordion" type="checkbox">
							<label for="sc-lb-module-faq-item-873859-3" class="item-wrapper">
								<span class="question">
									<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
									<span class="question-text">What are the differences between the annualised percentage rate (APR) and monthly flat rate of a personal loan?</span>
									<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
								</span>
							</label>
							<div class="answer">
								<ul>
<li>The APR of a personal loan is a reference loan interest rate which includes the basic interest rate and other applicable fees and charges of a product expressed as an annualised rate.</li>
<li>You may calculate the total loan interest expenses via monthly flat rate: Principal x Monthly Flat Rate x Tenor (months).</li>
</ul>
							</div>
						</li>
																				<li class="item">
							<input id="sc-lb-module-faq-item-873859-4" name="sc-lb-module-faq-item-accordion" type="checkbox">
							<label for="sc-lb-module-faq-item-873859-4" class="item-wrapper">
								<span class="question">
									<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
									<span class="question-text">Can I easily apply for SC Personal Instalment Loan without a Standard Chartered credit card?</span>
									<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
								</span>
							</label>
							<div class="answer">
								<p>It does not require a credit card to apply for a personal loan. If you have an emergency financial need but do not have a Standard Chartered credit card, you may consider a personal loan such as SC Personal Instalment Loan.</p>
							</div>
						</li>
												</ul>

							<ul class="list more-items">
																		<li class="item">
								<input id="sc-lb-module-faq-more-873859-0" name="sc-lb-module-faq-more-accordion" type="checkbox">
								<label for="sc-lb-module-faq-more-873859-0" class="item-wrapper">
									<span class="question">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<span class="question-text">If I want to borrow additional money, do I need to apply for another personal loan or any other loan?</span>
										<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
									</span>
								</label>
								<div class="answer">
									<p>If you are already a Standard Chartered Bank personal loan customer, you can apply for the Standard Chartered Personal Instalment Loan Top Up Service. This service allows you to borrow additional loan amount on top of your existing personal loan without further supporting documents required, addressing your immediate financial needs.</p>
								</div>
							</li>
																								<li class="item">
								<input id="sc-lb-module-faq-more-873859-1" name="sc-lb-module-faq-more-accordion" type="checkbox">
								<label for="sc-lb-module-faq-more-873859-1" class="item-wrapper">
									<span class="question">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<span class="question-text">Apart from using SC Personal Instalment Loan for cash out, what other bank loan options are available? What are the differences between these bank loan products?</span>
										<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
									</span>
								</label>
								<div class="answer">
									<ul>
<li>As aforementioned, Standard Chartered Bank offers <a href="https://sc.com/hk/loans/">loan products</a> such as credit card cash loans and Revolving Cash Card. To sum up, the differences between the instalment loan (Personal Loan), credit card cash loans and revolving loan are as follows:</li>
<li><strong>Instalment loan:</strong> Also known as ‘personal loan’, which is an unsecured loan that provides high loan amount and long repayment period. It is suitable for ones who needs a substantial loan. Personal loans generally have a lower loan interest rate compared to credit card cash overdraft, and can be quickly approved and disbursed. For example, SC Personal Instalment Loan accepts online application, and offers a personal loan amount of up to 18 times your monthly salary and a loan tenor of up to 60 months.</li>
<li><strong>Credit card cash loan:</strong> Credit card cash loans include cash advance, credit card overdraft and credit card statement instalment plan They are more commonly used for smaller loans as the borrowing limit on credit cards is typically the same as the credit limit. It is also noteworthy that the loan interest of credit card cash overdraft is calculated daily and potentially rise beyond 40%. Additional administrative fees and handling fees may also increase the borrowing cost.</li>
</ul>
								</div>
							</li>
																								<li class="item">
								<input id="sc-lb-module-faq-more-873859-2" name="sc-lb-module-faq-more-accordion" type="checkbox">
								<label for="sc-lb-module-faq-more-873859-2" class="item-wrapper">
									<span class="question">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<span class="question-text">Can I get an estimation of my monthly repayment amount in advance?</span>
										<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
									</span>
								</label>
								<div class="answer">
									<ul>
<li>Yes, you can use the <a href="https://sc.com/hk/loans/personal-instalment-loan-repayment-calculator/">Personal Instalment Loan Repayment Calculator</a> to calculate the monthly repayment amount, including the handling fee and APR.</li>
<li>The monthly repayment amount (including the principal amount and the handling fee per instalment) will be printed on the personal loan confirmation. Please refer to the monthly repayment table for details.</li>
</ul>
								</div>
							</li>
																								<li class="item">
								<input id="sc-lb-module-faq-more-873859-3" name="sc-lb-module-faq-more-accordion" type="checkbox">
								<label for="sc-lb-module-faq-more-873859-3" class="item-wrapper">
									<span class="question">
										<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
										<span class="question-text">More questions about Personal Loan?</span>
										<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
									</span>
								</label>
								<div class="answer">
									<ul>
<li>Visit <a href="https://sc.com/hk/help/loans/#sc-lb-module-eligibility-document">Help Centre – Loan</a><a href="https://www.sc.com/hk/help/loans/"></a> or call 3408 1628 for more information.</li>
</ul>
								</div>
							</li>
															</ul>
					</div>
					<div class="footer">
				<label for="faq-more-state-873859" class="read-more-trigger">
					<span class="read-more">
						<span class="c-button-load-more is-theme-hollow-gray is-size-fullwidth">
							<span class="button-load-more-content">
								Read More							</span>
						</span>
					</span>
					<span class="read-less">
						<span class="c-button-load-more is-theme-hollow-gray is-size-fullwidth">
							<span class="button-load-more-content">
								Read Less							</span>
						</span>
					</span>
				</label>
			</div>
			</div>
</div>

<div class="m-terms-conditions is-theme-gray" id="sc-lb-module-term-and-condition" data-post-status="publish-status" data-post-status-label="Published">
	<div class="content-wrapper">
							<div class="header">
				<h3 class="title">Terms and Conditions</h3>
			</div>
						<div class="content">
			<ul class="list">
									<li class="item link">
				<label class="item-wrapper">
					<a title="Terms and conditions for SC Personal Instalment Loan" data-context="Terms and conditions url link" href="https://av.sc.com/hk/content/docs/hk-loans-personal-instalment-loan-eng.pdf" target="_blank" rel="noopener noreferrer">						<span class="question">
							<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
							<span class="question-text">Terms and conditions for SC Personal Instalment Loan</span>
							<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
						</span>
					</a>
				</label>
			</li>
									<li class="item link">
				<label class="item-wrapper">
					<a title="Terms and conditions for SC Personal Instalment Loan Top-up Service" data-context="Terms and conditions url link" href="https://av.sc.com/hk/content/docs/hk-personal-instalment-loan-top-up-program-terms-and-conditions-en.pdf" target="_blank" rel="noopener noreferrer">						<span class="question">
							<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
							<span class="question-text">Terms and conditions for SC Personal Instalment Loan Top-up Service</span>
							<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
						</span>
					</a>
				</label>
			</li>
									<li class="item link">
				<label class="item-wrapper">
					<a title="Summary of Terms and conditions for SC Personal Instalment Loan / Personal Instalment Loan Top-up Service" data-context="Terms and conditions url link" href="https://sc.com/hk/help/customer-terms-and-conditions/" target="_blank" rel="noopener noreferrer">						<span class="question">
							<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
							<span class="question-text">Summary of Terms and conditions for SC Personal Instalment Loan / Personal Instalment Loan Top-up Service</span>
							<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
						</span>
					</a>
				</label>
			</li>
									<li class="item link">
				<label class="item-wrapper">
					<a title="Terms and Conditions for Bonus Payroll Account Welcome Offer" data-context="Terms and conditions url link" href="https://av.sc.com/hk/content/docs/hk-sbp-tnc-2025-q1-en.pdf" target="_blank" rel="noopener noreferrer">						<span class="question">
							<span class="c-icon icon-tick" style="background-image: none;"><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.118 11.137c-.201.198-.502.198-.803 0l-.1-.197-.201-.196-.803-.79L.6 6.21c-.201-.197-.201-.591 0-.788l1.103-1.183c.201-.197.502-.197.804 0l3.21 3.35L12.539.496c.2-.197.501-.197.802 0l1.104 1.183c.2.197.2.592 0 .788l-8.327 8.67z" fill="#38D54A"></path></svg></span>
							<span class="question-text">Terms and Conditions for Bonus Payroll Account Welcome Offer</span>
							<span class="c-icon icon-varrow" style="background-image: none;"><svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 1.4l-7 7H7l-7-7L1.3 0l6 6 6-6 1.4 1.4z" fill="#D5D5D5"></path></svg></span>
						</span>
					</a>
				</label>
			</li>
							</ul>

								</div>
			</div>
</div>
<link rel="stylesheet" id="sc-related-links-style-css" href="https://av.sc.com/assets/global/css/sc-related-links.min.css?ver=b0b95ac" media="all"><iframe sandbox="allow-scripts allow-same-origin" title="Adobe ID Syncing iFrame" id="destination_publishing_iframe_standchartbank_0" name="destination_publishing_iframe_standchartbank_0_name" src="https://standchartbank.demdex.net/dest5.html?d_nsid=0#https%3A%2F%2Fwww.sc.com" style="display: none; width: 0px; height: 0px;" class="aamIframeLoaded"></iframe>
<div class="sc-related-links " id="sc-lb-module-related-links" data-post-status="publish-status" data-post-status-label="Published">
	<div class="sc-related-links__wrapper">
		<h3 class="sc-related-links__title">
				Related Links		</h3>
		<div class="splide splide--slide splide--ltr splide--draggable is-active is-initialized" role="list" data-splide="{&quot;arrows&quot;:true,&quot;trimSpace&quot;:&quot;move&quot;,&quot;pagination&quot;:false,&quot;gap&quot;:&quot;16px&quot;,&quot;fixedWidth&quot;:&quot;250px&quot;,&quot;slideFocus&quot;:false,&quot;perPage&quot;:&quot;4&quot;,&quot;perMove&quot;:&quot;1&quot;,&quot;breakpoints&quot;:{&quot;1024&quot;:{&quot;perPage&quot;:&quot;2&quot;},&quot;680&quot;:{&quot;perPage&quot;:&quot;1&quot;}}}" id="splide01">
			<div class="splide__arrows"><button class="splide__arrow splide__arrow--prev" type="button" aria-controls="splide01-track" disabled="" aria-label="Previous slide"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" width="40" height="40"><path d="m15.5 0.932-4.3 4.38 14.5 14.6-14.5 14.5 4.3 4.4 14.6-14.6 4.4-4.3-4.4-4.4-14.6-14.6z"></path></svg></button><button class="splide__arrow splide__arrow--next" type="button" aria-controls="splide01-track" aria-label="Next slide"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" width="40" height="40"><path d="m15.5 0.932-4.3 4.38 14.5 14.6-14.5 14.5 4.3 4.4 14.6-14.6 4.4-4.3-4.4-4.4-14.6-14.6z"></path></svg></button></div><div class="splide__track" id="splide01-track" style="padding-left: 0px; padding-right: 0px;">
				<div class="splide__list sc-related-links__list" role="list" id="splide01-list" style="transform: translateX(0px);">
											<div class="splide__slide is-active is-visible" role="listitem" id="splide01-slide01" style="margin-right: 16px; width: 250px;">
							<a title="Personal Instalment Loan Top Up Service" data-context="Related link list link" href="https://www.sc.com/hk/loans/personal-instalment-loan/topup/">
								<div class="sc-card-tile">
									<div class="sc-card-tile__link">
																					<div class="sc-card-tile__icon icon-link" aria-hidden="true" style="background-image: none;"><svg width="24" height="16" viewBox="0 0 24 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.117.856C11.254.856 8.11 4 8.11 8h2c0-3 2.246-5.144 5.007-5.144 2.762 0 4.95 2.308 4.95 5.144 0 2.837-2.067 5.144-5.067 5.144v2c4 0 7.066-3.205 7.066-7.144S18.981.856 15.117.856z" fill="#000"></path><path d="M7.863 13.144c-2.76 0-4.939-2.308-4.939-5.145C2.924 5.163 5 2.856 8 2.856v-2C4 .856.924 4.06.924 8s3.11 7.145 6.973 7.145C11.761 15.145 14.87 12 14.87 8h-2c0 3-2.246 5.144-5.007 5.144z" fill="#000"></path></svg></div>
																							<div class="sc-card-tile__tile-image">
			<img width="400" height="400" src="https://av.sc.com/hk/content/images/hk-loans-pil-rl-oct24-400-400.png" class="sc-card-tile__tile-img" alt="Hk loans pil rl oct " loading="lazy" decoding="async">			</div>
													<div class="sc-card-tile__content">
																						<h3 class="sc-card-tile__title">Personal Instalment Loan Top Up Service</h3>
										</div>
									</div>
								</div>
							</a>
						</div>
											<div class="splide__slide is-visible is-next" role="listitem" id="splide01-slide02" style="margin-right: 16px; width: 250px;">
							<a title="Debt Consolidation Programme" data-context="Related link list link" href="https://www.sc.com/hk/loans/debt-consolidation/?intcid=nav_dc_t">
								<div class="sc-card-tile">
									<div class="sc-card-tile__link">
																					<div class="sc-card-tile__icon icon-link" aria-hidden="true" style="background-image: none;"><svg width="24" height="16" viewBox="0 0 24 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.117.856C11.254.856 8.11 4 8.11 8h2c0-3 2.246-5.144 5.007-5.144 2.762 0 4.95 2.308 4.95 5.144 0 2.837-2.067 5.144-5.067 5.144v2c4 0 7.066-3.205 7.066-7.144S18.981.856 15.117.856z" fill="#000"></path><path d="M7.863 13.144c-2.76 0-4.939-2.308-4.939-5.145C2.924 5.163 5 2.856 8 2.856v-2C4 .856.924 4.06.924 8s3.11 7.145 6.973 7.145C11.761 15.145 14.87 12 14.87 8h-2c0 3-2.246 5.144-5.007 5.144z" fill="#000"></path></svg></div>
																							<div class="sc-card-tile__tile-image">
			<img width="400" height="400" src="https://av.sc.com/hk/content/images/hk-loans-dc-nov24-pintile-400-400-en.jpg" class="sc-card-tile__tile-img" alt="Hk loans dc nov pintile en" loading="lazy" decoding="async">			</div>
													<div class="sc-card-tile__content">
																						<h3 class="sc-card-tile__title">Debt Consolidation Programme</h3>
										</div>
									</div>
								</div>
							</a>
						</div>
											<div class="splide__slide is-visible" role="listitem" id="splide01-slide03" style="margin-right: 16px; width: 250px;">
							<a title="Financial Analysis" data-context="Related link list link" href="https://www.sc.com/hk/loans/financial-analysis/">
								<div class="sc-card-tile">
									<div class="sc-card-tile__link">
																					<div class="sc-card-tile__icon icon-link" aria-hidden="true" style="background-image: none;"><svg width="24" height="16" viewBox="0 0 24 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.117.856C11.254.856 8.11 4 8.11 8h2c0-3 2.246-5.144 5.007-5.144 2.762 0 4.95 2.308 4.95 5.144 0 2.837-2.067 5.144-5.067 5.144v2c4 0 7.066-3.205 7.066-7.144S18.981.856 15.117.856z" fill="#000"></path><path d="M7.863 13.144c-2.76 0-4.939-2.308-4.939-5.145C2.924 5.163 5 2.856 8 2.856v-2C4 .856.924 4.06.924 8s3.11 7.145 6.973 7.145C11.761 15.145 14.87 12 14.87 8h-2c0 3-2.246 5.144-5.007 5.144z" fill="#000"></path></svg></div>
																							<div class="sc-card-tile__tile-image">
			<img width="400" height="400" src="https://av.sc.com/hk/content/images/hk-loans-financial-analysis-rl.jpg" class="sc-card-tile__tile-img" alt="Hk loans financial analysis rl" loading="lazy" decoding="async">			</div>
													<div class="sc-card-tile__content">
																						<h3 class="sc-card-tile__title">Financial Analysis</h3>
										</div>
									</div>
								</div>
							</a>
						</div>
											<div class="splide__slide is-visible" role="listitem" id="splide01-slide04" style="margin-right: 16px; width: 250px;">
							<a title="LendWise: Online Loan Insights &amp; Tips" data-context="Related link list link" href="https://www.sc.com/hk/loans/loan-tips/">
								<div class="sc-card-tile">
									<div class="sc-card-tile__link">
																					<div class="sc-card-tile__icon icon-link" aria-hidden="true" style="background-image: none;"><svg width="24" height="16" viewBox="0 0 24 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.117.856C11.254.856 8.11 4 8.11 8h2c0-3 2.246-5.144 5.007-5.144 2.762 0 4.95 2.308 4.95 5.144 0 2.837-2.067 5.144-5.067 5.144v2c4 0 7.066-3.205 7.066-7.144S18.981.856 15.117.856z" fill="#000"></path><path d="M7.863 13.144c-2.76 0-4.939-2.308-4.939-5.145C2.924 5.163 5 2.856 8 2.856v-2C4 .856.924 4.06.924 8s3.11 7.145 6.973 7.145C11.761 15.145 14.87 12 14.87 8h-2c0 3-2.246 5.144-5.007 5.144z" fill="#000"></path></svg></div>
																							<div class="sc-card-tile__tile-image">
			<img width="536" height="460" src="https://av.sc.com/hk/content/images/hk-03-International-Banking.jpg" class="sc-card-tile__tile-img" alt="Hk international banking" loading="lazy" decoding="async" srcset="https://av.sc.com/hk/content/images/hk-03-International-Banking.jpg 536w, https://av.sc.com/hk/content/images/hk-03-International-Banking-408x350.jpg 408w" sizes="(max-width: 536px) 100vw, 536px">			</div>
													<div class="sc-card-tile__content">
																						<h3 class="sc-card-tile__title">LendWise: Online Loan Insights &amp; Tips</h3>
										</div>
									</div>
								</div>
							</a>
						</div>
											<div class="splide__slide" role="listitem" id="splide01-slide05" style="margin-right: 16px; width: 250px;" aria-hidden="true">
							<a title="Call our Hotline : (852)2179-2800" data-context="Related link list link" href="tel:(852)2179-2800" tabindex="-1">
								<div class="sc-card-tile">
									<div class="sc-card-tile__link">
																					<div class="sc-card-tile__icon icon-link" aria-hidden="true" style="background-image: none;"><svg width="24" height="16" viewBox="0 0 24 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.117.856C11.254.856 8.11 4 8.11 8h2c0-3 2.246-5.144 5.007-5.144 2.762 0 4.95 2.308 4.95 5.144 0 2.837-2.067 5.144-5.067 5.144v2c4 0 7.066-3.205 7.066-7.144S18.981.856 15.117.856z" fill="#000"></path><path d="M7.863 13.144c-2.76 0-4.939-2.308-4.939-5.145C2.924 5.163 5 2.856 8 2.856v-2C4 .856.924 4.06.924 8s3.11 7.145 6.973 7.145C11.761 15.145 14.87 12 14.87 8h-2c0 3-2.246 5.144-5.007 5.144z" fill="#000"></path></svg></div>
																							<div class="sc-card-tile__tile-image">
			<img width="400" height="400" src="https://av.sc.com/hk/content/images/hk-loans-pil-rl-oct24-400-400.png" class="sc-card-tile__tile-img" alt="Hk loans pil rl oct " loading="lazy" decoding="async">			</div>
													<div class="sc-card-tile__content">
																						<h3 class="sc-card-tile__title">Call our Hotline : (852)2179-2800</h3>
										</div>
									</div>
								</div>
							</a>
						</div>
									</div>
			</div>
		</div>
	</div>
</div>
<link rel="stylesheet" id="sc-persistent-bar-new-style-css" href="https://av.sc.com/assets/global/css/persistent-bar-btn-animation.min.css?ver=b0b95ac" media="all">

<!-- Persistent Bar -->
<div class="m-persistent-bootom-bar btn-animated" id="sc-lb-module-persistent-bar-new" data-post-status="publish-status" data-post-status-label="Published">
		<div class="column">
		<label class="title">
							<span class="mobile">APR as low as 1.85% and up to HKD18,000 cash rebate</span>
										<span class="desktop">APR as low as 1.85% and up to HKD18,000 cash rebate</span>
					</label>
	</div>
	<div class="column apply-now">
		<ul class="buttons">
												<li>
					<a href="https://origination.sc.com/onboarding/hk/apply.html?product=1258&amp;campaign=HKPIL23PLSTP10&amp;premium=1258&amp;cardType=3268&amp;affiliation=2132&amp;lang=en" title="Apply Now" data-context="Persistent Bar CTA" class="c-button c-button is-theme-solid-green-hollow-white rounded-button apply-now-button" target="_blank" rel="noopener noreferrer" data-widget-name="persistent bar">
			<span class="only-desktop">Apply Now</span>
							<span class="only-mobile">Apply Now</span>
					</a>
	</li>
									</ul>
	</div>
	</div>
<link rel="stylesheet" id="sc-hk-pro-content-sec-style-css" href="https://av.sc.com/assets/global/css/hk-promotions-content-section.min.css?ver=b0b95ac" media="all">

	<div class="m-promotions-content-section" id="sc-lb-module-hk-pro-content-sec" data-post-status="publish-status" data-post-status-label="Published">
		<div class="m-promotions-content-section__content m-promotions-content-section__text-center">
			<p class="m-promotions-content-section__message">
				To borrow or not to borrow? Borrow only if you can repay!			</p>
		</div>
	</div>
<footer class="m-footer has-columns" id="sc-lb-module-footer" data-post-status="publish-status" data-post-status-label="Published">
	<div class="content-wrapper">
		<div class="site-info only-desktop">
							<span class="company">© Standard Chartered Bank (HK) Limited</span>
										<span class="sitemap">
					<a title="Site map" data-context="Footer site map link" href="https://www.sc.com/hk/sitemap/">						Sitemap					</a>
				</span>
					</div>

		
		<div class="column only-desktop">
			<ul class="list">
									<li>
						<a title="About Us" data-context="Footer left column links" href="https://www.sc.com/hk/about-us/">								About Us							</a>
												</li>
									<li>
						<a title="Investor Relations" data-context="Footer left column links" href="https://www.sc.com/hk/investor-relations/">								Investor Relations							</a>
												</li>
									<li>
						<a title="News &amp; Media" data-context="Footer left column links" href="https://www.sc.com/hk/news-media/">								News &amp; Media							</a>
												</li>
									<li>
						<a title="Help Centre" data-context="Footer left column links" href="https://www.sc.com/hk/help/">								Help Centre							</a>
												</li>
									<li>
						<a title="Forms and Documents" data-context="Footer left column links" href="https://www.sc.com/hk/help/download-centre/">								Forms and Documents							</a>
												</li>
									<li>
						<a title="Service Charges" data-context="Footer left column links" href="https://www.sc.com/hk/help/service-charges/">								Service Charges							</a>
												</li>
									<li>
						<a title="ATMs &amp; Branches" data-context="Footer left column links" href="https://www.sc.com/hk/atm-branch-locator/">								ATMs &amp; Branches							</a>
												</li>
									<li>
						<a title="Contact Us" data-context="Footer left column links" href="https://www.sc.com/hk/help/contact-us/">								Contact Us							</a>
												</li>
							</ul>
		</div>

		<div class="column only-desktop">
			<ul class="list">
									<li>
						<a title="Careers" data-context="Footer left column links" href="https://www.sc.com/en/careers/" target="_blank" rel="noopener noreferrer">								Careers							</a>
												</li>
									<li>
						<a title="Global Research" data-context="Footer left column links" href="https://www.sc.com/en/banking/banking-for-companies/global-research/" target="_blank" rel="noopener noreferrer">								Global Research							</a>
												</li>
									<li>
						<a title="Speaking Up" data-context="Footer left column links" href="http://www.speakingupsc.ethicspoint.com/" target="_blank" rel="noopener noreferrer">								Speaking Up							</a>
												</li>
									<li>
						<a title="Protecting our clients" data-context="Footer left column links" href="https://www.sc.com/protecting-our-clients/" target="_blank" rel="noopener noreferrer">								Protecting our clients							</a>
												</li>
									<li>
						<a title="Fighting Fraud" data-context="Footer left column links" href="https://www.sc.com/en/about/fighting-financial-crime/fighting-fraud/personal-account/" target="_blank" rel="noopener noreferrer">								Fighting Fraud							</a>
												</li>
									<li>
						<a title="Security Tips" data-context="Footer left column links" href="https://www.sc.com/global/security-tips/" target="_blank" rel="noopener noreferrer">								Security Tips							</a>
												</li>
									<li>
						<a title="Sustainability" data-context="Footer left column links" href="https://www.sc.com/hk/sustainability/">								Sustainability							</a>
												</li>
									<li>
						<a title="Group Website" data-context="Footer left column links" href="https://www.sc.com/en/" target="_blank" rel="noopener noreferrer">								Group Website							</a>
												</li>
							</ul>
		</div>

		<div class="column only-desktop ">
			<ul class="list">
									<li>
						<a title="Important Notice" data-context="Footer left column links" href="https://www.sc.com/hk/online-banking/notice/">								Important Notice							</a>
												</li>
									<li>
						<a title="Regulatory Disclosures" data-context="Footer left column links" href="https://www.sc.com/hk/regulatory-disclosures/">								Regulatory Disclosures							</a>
												</li>
									<li>
						<a title="Locations of the Bank's Service Providers" data-context="Footer left column links" href="https://www.sc.com/hk/online-banking/notice/#location">								Locations of the Bank's Service Providers							</a>
												</li>
									<li>
						<a title="Terms &amp; Conditions" data-context="Footer left column links" href="https://www.sc.com/hk/terms-and-conditions/disclaimer/">								Terms &amp; Conditions							</a>
												</li>
									<li>
						<a title="Cookie Policy" data-context="Footer left column links" href="https://www.sc.com/hk/cookie-policy/" target="_blank" rel="noopener noreferrer">								Cookie Policy							</a>
												</li>
									<li>
						<a title="PRIVACY NOTICE" data-context="Footer left column links" href="/hk/privacy-notice/" target="_blank" rel="noopener noreferrer">								PRIVACY NOTICE							</a>
												</li>
									<li>
						<a title="PERSONAL INFORMATION COLLECTION STATEMENT" data-context="Footer left column links" href="https://av.sc.com/hk/content/docs/hk-gn050-v2-nov23.pdf">								PERSONAL INFORMATION COLLECTION STATEMENT							</a>
												</li>
									<li>
						<a title="Open banking" data-context="Footer left column links" href="https://www.sc.com/hk/bank-with-us/open-banking/">								Open banking							</a>
												</li>
							</ul>
		</div>

		<div class="column"><div class="c-language-selector" data-catch="update-language" data-language-sel="en"><div class="buttons"><button class="c-button is-active" data-send="update-language" data-language="en">En</button><button class="c-button" data-send="update-language" data-language="zh">中文</button></div></div>
												<div class="other-images">
																																														</div>
											<div class="contact-data">
																										<ul class="segment">
														<li>
																			<h3>We are here to help </h3>
																																														<p class="email-title">Check out latest FAQ, forms and other useful information</p>
																													<p class="email">
												<a href="mailto:HelpCentre">
														Help Centre												</a>
											</p>
																			</li>
														</ul>
									</div>
													<div class="accordion-item">
					<div class="item-wrapper only-mobile">
						<input id="footer-quick-links-10814" name="footer-quick-links-10814" type="checkbox">
						<label for="footer-quick-links-10814">
							<span class="question">
								<span class="question-text">Quick Links</span>
								<span class="icon-down-arrow">
									<svg width="10" xmlns="http://www.w3.org/2000/svg" viewBox="-10 13.2 14.7 8.4">
										<style type="text/css">
											.st0{fill:#D5D5D5;}
										</style>
										<path class="st0" d="M4.7 14.6l-7 7H-3l-7-7 1.3-1.4 6 6 6-6L4.7 14.6z"></path>
									</svg>
								</span>
							</span>
						</label>
						<div class="answer">
							<ul>
																	<li>
										<a title="PRIVACY NOTICE" data-context="Footer mobile links" href="/hk/privacy-notice/">											PRIVACY NOTICE										</a>
									</li>
															</ul>
						</div>
					</div>
				</div>
			
			<ul class="social-links">
										<li>
								<a title="Linked In" data-context="Footer social media links" href="https://www.linkedin.com/company/standardchartered/">									<svg width="21" height="20" viewBox="0 0 21 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M20.01 12.444V20h-3.952v-7.05c0-1.77-.794-2.98-2.393-2.98-1.22 0-2.307.815-2.627 1.604-.117.282-.146.673-.146 1.068V20H6.938s.06-11.735 0-12.972h4.107v1.664l-.03.042h.03v-.042c.587-.896 1.843-2.177 4.189-2.177 2.906-.001 4.777 1.882 4.777 5.929zM1.18 20h3.849V7.028h-3.85V20zM3.094 0c1.501 0 2.719 1.042 2.719 2.328 0 1.286-1.217 2.328-2.719 2.328-1.502 0-2.719-1.042-2.719-2.328C.375 1.042 1.592 0 3.094 0z" fill="#434343"></path></svg>								</a>
							</li>
														<li>
								<a title="Facebook" data-context="Footer social media links" href="https://www.facebook.com/standardcharteredhk/">									<svg width="11" height="20" viewBox="0 0 11 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.013 10.398h-3.09v9.111h-3.82v-9.111H.993V7.397h2.11V4.37c0-1.514.804-3.88 3.826-3.88l3.388.011v3.693H7.426c-.322 0-.502.168-.502.89v2.314h3.409l-.32 3z" fill="#434343"></path></svg>								</a>
							</li>
														<li>
								<a title="Twitter" data-context="Footer social media links" href="https://twitter.com/StanChart">									<svg width="23" height="23" viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21.025 19.59c-2.428-3.24-4.86-6.483-7.289-9.727l-1.062 1.128c2.376 3.173 4.755 6.342 7.135 9.51.044.058.088.115.132.177H16.87l-5.84-7.933-1.062 1.133c1.402 1.904 2.803 3.808 4.204 5.707l1.93 2.618H23c-.666-.868-1.318-1.741-1.975-2.614zM3.301 2.251h2.816l2.37 3.165c1.076 1.432 2.151 2.869 3.226 4.3.353-.378.706-.753 1.063-1.127C10.81 5.972 8.845 3.35 6.878.728H.277c1.86 2.525 3.715 5.05 5.575 7.575 1.058 1.432 2.111 2.86 3.164 4.292.353-.379.705-.753 1.063-1.132L3.3 2.253z" fill="#434343"></path><path d="M11.03 12.75c-.356.379-.709.758-1.061 1.132-1.785 1.904-3.574 3.808-5.36 5.707-.819.873-1.634 1.745-2.454 2.618H0l2.455-2.618 3.41-3.635c1.054-1.12 2.103-2.24 3.156-3.363.353-.379.705-.753 1.062-1.132l.948 1.29zM22.313.723c-2.86 3.045-5.72 6.095-8.576 9.14l-1.062 1.128-.961-1.282c.352-.379.705-.754 1.062-1.128 2.459-2.618 4.914-5.24 7.373-7.862h2.164v.004z" fill="#434343"></path><path d="M21.025 19.59c-2.428-3.24-4.86-6.483-7.289-9.727l-1.062 1.128c2.376 3.173 4.755 6.342 7.135 9.51.044.058.088.115.132.177H16.87l-5.84-7.933-1.062 1.133c1.402 1.904 2.803 3.808 4.204 5.707l1.93 2.618H23c-.666-.868-1.318-1.741-1.975-2.614zM3.301 2.251h2.816l2.37 3.165c1.076 1.432 2.151 2.869 3.226 4.3.353-.378.706-.753 1.063-1.127C10.81 5.972 8.845 3.35 6.878.728H.277c1.86 2.525 3.715 5.05 5.575 7.575 1.058 1.432 2.111 2.86 3.164 4.292.353-.379.705-.753 1.063-1.132L3.3 2.253z" fill="#434343"></path><path d="M11.03 12.75c-.356.379-.709.758-1.061 1.132-1.785 1.904-3.574 3.808-5.36 5.707-.819.873-1.634 1.745-2.454 2.618H0l2.455-2.618 3.41-3.635c1.054-1.12 2.103-2.24 3.156-3.363.353-.379.705-.753 1.062-1.132l.948 1.29zM22.313.723c-2.86 3.045-5.72 6.095-8.576 9.14l-1.062 1.128-.961-1.282c.352-.379.705-.754 1.062-1.128 2.459-2.618 4.914-5.24 7.373-7.862h2.164v.004z" fill="#434343"></path></svg>								</a>
							</li>
										</ul>
		</div>

		<div class="clearer"></div>
	</div>
</footer>

<div class="m-click-to-chat chatbot" id="sc-lb-module-click-to-chat" data-post-status="publish-status" data-post-status-label="Published" data-video="" data-audio="" data-text="Stacy" data-modal-title="" data-modal-message="" data-modal-cancel-lbl="" data-modal-cta-lbl="" data-chatbot-url="https://av.sc.com/assets/global/chatbot/hk/en/index.html" data-chatbot-name="Stacy" data-chatbot-title="Stacy" data-chatbot-subtitle="Typically replies instantly" data-chatbot-avatar-icon-name="" data-chatbot-greeting-name="" data-chatbot-in-chat-icon-name="" data-chatbot-prompt="1" data-chatbot-prompt-text="Need help?" data-chatbot-prompt-appear-delay="2000" data-chatbot-prompt-disappear-delay="15000" data-chatbot-prompt-disappear="1" data-subject-id="HK_BORROW_PERSONAL_INSTALMENT_LOAN_EN" data-entry-type="HK_UC12_EN" data-work-group="HK_SALES_CHAT_PAGE" data-button-mode="false" data-animation-type="bounceInRight" data-trigger-time="30"></div>
			<script type="application/ld+json">
		{"@context":"http:\/\/schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How to determine the personal loan amount and loan repayment period?","acceptedAnswer":{"@type":"Answer","text":"<ul>\r\n \t<li>When applying for a personal loan, it is crucial to evaluate personal repayment capacity objectively. Ideally, you should only borrow the amount of money you truly need, in order to avoid excessive borrowing.<\/li>\r\n \t<li>While calculating the cost of borrowing personal loan, it’s important to include any administrative fee, handling fee and other additional costs associated with personal loan SC Personal Instalment Loan is a bank loan that is free of handling fee, reducing your borrowing costs.<\/li>\r\n \t<li>You may also utilize our <a href=\"https:\/\/sc.com\/hk\/loans\/personal-instalment-loan-repayment-calculator\/\">Standard Chartered’s Personal Instalment Loan Repayment Calculator<\/a> to quickly estimate your monthly repayment amount as a reference for your financial planning and budgeting for your personal loan.<\/li>\r\n<\/ul>"}},{"@type":"Question","name":"What are the eligibility criteria for applying for a personal loan?","acceptedAnswer":{"@type":"Answer","text":"<ul>\r\n \t<li>It is not difficult to be eligible for a Personal Loan. For instance, for SC Personal Instalment Loan, Hong Kong residents aged 20 or above with a fixed annual income of HKD96,000 or above are eligible to apply.<\/li>\r\n<\/ul>"}},{"@type":"Question","name":"Can I make an early repayment for my personal loan?","acceptedAnswer":{"@type":"Answer","text":"<ul>\r\n \t<li>You have the flexibility to repay the personal loan In additional to the personal loan instalment amount, you must settle all accrued but unpaid loan interest up to the actual settlement date, an early settlement fee of 2.5% of the outstanding balance and any other sum due to us. If the personal loan repayment is made within the 7-Day Cooling-off Period, early redemption fees would be waived. Please note that the bank reserves the right to request the full refund of any cash rebate received during the application or deduct the equivalent value of the cash rebate from any account of the eligible customer.<\/li>\r\n \t<li>If you plan to repay the personal loan in full early, you must notify us in writing ten business days before your proposed repayment date.<\/li>\r\n<\/ul>"}},{"@type":"Question","name":"What are the differences between the annualised percentage rate (APR) and monthly flat rate of a personal loan?","acceptedAnswer":{"@type":"Answer","text":"<ul>\r\n \t<li>The APR of a personal loan is a reference loan interest rate which includes the basic interest rate and other applicable fees and charges of a product expressed as an annualised rate.<\/li>\r\n \t<li>You may calculate the total loan interest expenses via monthly flat rate: Principal x Monthly Flat Rate x Tenor (months).<\/li>\r\n<\/ul>"}},{"@type":"Question","name":"Can I easily apply for SC Personal Instalment Loan without a Standard Chartered credit card?","acceptedAnswer":{"@type":"Answer","text":"It does not require a credit card to apply for a personal loan. If you have an emergency financial need but do not have a Standard Chartered credit card, you may consider a personal loan such as SC Personal Instalment Loan."}},{"@type":"Question","name":"If I want to borrow additional money, do I need to apply for another personal loan or any other loan?","acceptedAnswer":{"@type":"Answer","text":"If you are already a Standard Chartered Bank personal loan customer, you can apply for the Standard Chartered Personal Instalment Loan Top Up Service. This service allows you to borrow additional loan amount on top of your existing personal loan without further supporting documents required, addressing your immediate financial needs."}},{"@type":"Question","name":"Apart from using SC Personal Instalment Loan for cash out, what other bank loan options are available? What are the differences between these bank loan products?","acceptedAnswer":{"@type":"Answer","text":"<ul>\r\n \t<li>As aforementioned, Standard Chartered Bank offers <a href=\"https:\/\/sc.com\/hk\/loans\/\">loan products<\/a> such as credit card cash loans and Revolving Cash Card. To sum up, the differences between the instalment loan (Personal Loan), credit card cash loans and revolving loan are as follows:<\/li>\r\n \t<li><strong>Instalment loan:<\/strong> Also known as ‘personal loan’, which is an unsecured loan that provides high loan amount and long repayment period. It is suitable for ones who needs a substantial loan. Personal loans generally have a lower loan interest rate compared to credit card cash overdraft, and can be quickly approved and disbursed. For example, SC Personal Instalment Loan accepts online application, and offers a personal loan amount of up to 18 times your monthly salary and a loan tenor of up to 60 months.<\/li>\r\n \t<li><strong>Credit card cash loan:<\/strong> Credit card cash loans include cash advance, credit card overdraft and credit card statement instalment plan They are more commonly used for smaller loans as the borrowing limit on credit cards is typically the same as the credit limit. It is also noteworthy that the loan interest of credit card cash overdraft is calculated daily and potentially rise beyond 40%. Additional administrative fees and handling fees may also increase the borrowing cost.<\/li>\r\n<\/ul>"}},{"@type":"Question","name":"Can I get an estimation of my monthly repayment amount in advance?","acceptedAnswer":{"@type":"Answer","text":"<ul>\r\n \t<li>Yes, you can use the <a href=\"https:\/\/sc.com\/hk\/loans\/personal-instalment-loan-repayment-calculator\/\">Personal Instalment Loan Repayment Calculator<\/a> to calculate the monthly repayment amount, including the handling fee and APR.<\/li>\r\n \t<li>The monthly repayment amount (including the principal amount and the handling fee per instalment) will be printed on the personal loan confirmation. Please refer to the monthly repayment table for details.<\/li>\r\n<\/ul>"}},{"@type":"Question","name":"More questions about Personal Loan?","acceptedAnswer":{"@type":"Answer","text":"<ul>\r\n \t<li>Visit <a href=\"https:\/\/sc.com\/hk\/help\/loans\/#sc-lb-module-eligibility-document\">Help Centre – Loan<\/a><a href=\"https:\/\/www.sc.com\/hk\/help\/loans\/\"><\/a> or call 3408 1628 for more information.<\/li>\r\n<\/ul>"}}]}	</script>
	
<div class="helper-svg-gradients">
	<svg width="100px" height="100px" viewBox="0 0 100 100">
		<defs>
			<!-- Gradient from blue to green -->
			<linearGradient id="gradient-blue-to-green" gradientUnits="userSpaceOnUse" x1="0%" y1="0%" x2="100%" y2="100%">
				<stop stop-color="#6cc9fe" offset="0"></stop>
				<stop stop-color="#38d54a" offset="1"></stop>
			</linearGradient>
		</defs>
	</svg>
</div>


<script src="https://av.sc.com/assets/global/js/vendor/jquery-3.5.1.min.js" id="jquery-js"></script>
<script src="https://av.sc.com/assets/global/js/vendor.min.js?ver=b0b95ac" id="vendor-js"></script>
<script src="https://av.sc.com/assets/global/icons/grunticon.loader.min.js?ver=b0b95ac" id="grunticon-js"></script>
<script src="https://av.sc.com/assets/global/js/vendor/bundle.min.js?ver=b0b95ac" id="bundlejs-js"></script>
<script src="https://av.sc.com/assets/global/js/grunticon-init.min.js?ver=b0b95ac" id="grunticon-init-js"></script>
<script src="https://av.sc.com/assets/global/js/analytics/cs/contentsquare-custom.min.js?ver=b0b95ac" id="contentsquare-custom-script-js"></script><link rel="stylesheet" href="https://www.sc.com/assets/global/icons/icons.data.svg.css" media="all">
<script src="https://av.sc.com/assets/global/js/onetrust-cookie-custom.min.js?ver=b0b95ac" id="sc-onetrust-cookie-script-js"></script>
<script src="https://av.sc.com/assets/global/js/vendor/nouislider.min.js?ver=b0b95ac" id="nouislider_script-js"></script>
<script src="https://av.sc.com/assets/global/js/sc-hk-pil-calculator.min.js?ver=b0b95ac" id="sc-hk-pil-calculator-script-js"></script>
<script src="https://av.sc.com/assets/global/js/product-key-features.min.js?ver=b0b95ac" id="sc-hk-product-feature-script-js"></script>
<script src="https://av.sc.com/assets/global/js/clickToChat.min.js?ver=b0b95ac" id="clicktochat-js"></script>
<script>
		if(typeof _satellite !== "undefined") {
		_satellite.pageBottom();
		}
		</script><script>(function () {
  addEventListener('load', function() {
    window._uxa = window._uxa || [];
    try {
        if (typeof digitalData !== 'undefined') {
			window._uxa.push(['setCustomVariable', 1, 'pageName', digitalData.page.pageInfo.pageName]);
			window._uxa.push(['setCustomVariable', 2, 'primaryCategory', digitalData.page.category.primaryCategory]);
			window._uxa.push(['setCustomVariable', 3, 'subCategory1', digitalData.page.category.subCategory1]);
			window._uxa.push(['setCustomVariable', 4, 'subCategory2', digitalData.page.category.subCategory2]);
        }
    } catch(e){}
    if (typeof CS_CONF === 'undefined') {
        window._uxa.push(['setPath', window.location.pathname+window.location.hash.replace('#','?__')]);
        var mt = document.createElement('script'); mt.type = 'text/javascript'; mt.async = true;
        mt.src = '//t.contentsquare.net/uxa/3bdacf36a16df.js';
        document.getElementsByTagName('head')[0].appendChild(mt);
    }
    else {
        window._uxa.push(['trackPageview', window.location.pathname+window.location.hash.replace('#','?__')]);
    }
  });
})();
</script>
<script type="text/javascript" src="/rOaFmT/HR/_5/XVdU/lwhvgQ1YWX3ZY/3SzaprptViDSkiYE/c3wnAQ/UycMZWE/jDWs"></script>

<div class="c2c_modal_wrapper"><div class="c2c_modal_content_wrapper"><div class="c2c_modal_content"><div class="c2c_modal_content_title">Alert!</div><div class="c2c_modal_content_message"></div></div></div><div class="c2c_modal_buttons"><input type="button" value="Cancel" class="c2c_cancel_btn"><input type="button" value="Proceed" class="c2c_proceed_btn"></div><div class="c2c_modal_close"></div></div><div class="c2c c2c_box_wrapper bounceInRight animated c2c_right_position c2c_click_mode visible"><div class="chatbot-icon-wrapper"><span class="chatbot-prompt" style="">Need help?</span><img src="https://av.sc.com/assets/global/chatbot/images/chatbot-avatar.png" class="chatbot-avatar icon-sc-chatbot-avatar-round" id="chatbot-icon" style="cursor: pointer;"></div><div class="c2c_content c2c_layout_right_position" style="display: none;"><div class="scformsikon scformsikon-chat c2c_bubble"><img class="c2c_ikon" alt="value" src="https://av.sc.com/assets/global/images/modules/click-to-chat/scformsikon-chat.svg" onerror="this.src='https://av.sc.com/assets/global/images/modules/click-to-chat/scformsikon-chat.png'; this.onerror=null;"><div class="c2c-title-text">Click to Chat</div></div><ul class="c2c_list"><li class="c2c_action chatOption2 option_chat hover"> <img class="c2c_ikon" alt="value" src="https://av.sc.com/assets/global/images/modules/click-to-chat/scformsikon-chat.svg" onerror="this.src='https://av.sc.com/assets/global/images/modules/click-to-chat/scformsikon-chat.png'; this.onerror=null;"><div class="c2c_text_content">Stacy</div></li></ul></div><div class="c2c_help_text bottomRight action-enable hide"> <div class="help-text-wrapper"><span>false</span><div class="close-help-text"></div></div><div class="border-triangle"></div></div></div><script>
!function(){function e(e){window.dataWidgetName=e.currentTarget.dataset.widgetName,console.log(`Clicked: ${e.currentTarget.title}, data-widget-name set to: ${window.dataWidgetName}`)}function t(e){const t=e.dataset.context||"",a=e.closest("div"),n=a?a.parentElement:null,c=n?n.parentElement:null;let s="na";if("Masthead CTA"===t||"Product Masthead CTA"===t)s="masthead";else if("Banner CTA"===t&&c?.className.includes("web-three-one"))s="carousel";else if("Banner CTA"===t)s="banner";else if(t?.includes("Promotional"))s="promotions";else if(t?.includes("Persistent")||t?.includes("Calculator")&&n?.className.includes("sticky"))s="persistent bar";else if(t?.includes("Bottom")&&c?.className.includes("sticky"))s="persistent bar";else if(t?.includes("Comparator")||"Product CTA"===t)s="comparator";else{const e=a?.className||"",t=n?.className||"";s=e.includes("bnr")||e.includes("banner")?"masthead":e.includes("accordion")?"accordion":e.includes("calc")?"calculator":e.includes("meganav")?"top nav":e.includes("card")?"card":e.includes("tab")?"tab":e.includes("compare")?"comparator":e.includes("persistent")?"persistent bar":t.includes("bnr")||t.includes("banner")?"masthead":t.includes("accordion")||t.includes("accordian")?"accordion":t.includes("calc")?"calculator":t.includes("compare")?"comparator":t.includes("persistent")?"persistent bar":"na"}return s}function a(){const s=50;for(let a=0;a<s&&c<n.length;a++,c++){const a=n[c];a.setAttribute("data-widget-name",t(a)),a.addEventListener("click",e)}c<n.length&&requestAnimationFrame(a)}var n=document.querySelectorAll('a.sc-btn[title*="apply" i], a.apply-now-button[title*="apply" i], a.c-button[title*="apply" i], a.sc-btn[data-context*="CTA" i], a.sc-btn[data-context*="Promotional" i], a.sc-btn[data-context*="Persistent" i], a.sc-btn[data-context*="Calculator" i], a.sc-btn[data-context*="Bottom" i], a.sc-btn[data-context*="Comparator" i]');let c=0;requestAnimationFrame(a)}();
</script>
<script type="text/javascript" id="" charset="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init",google_tag_manager["rm"]["381932"](40));fbq("track","PageView");</script>
<noscript>
 <img height="1" width="1" src="https://www.facebook.com/tr?id=621295738320142&amp;ev=PageView
&amp;noscript=1">
</noscript><iframe height="0" width="0" style="display: none; visibility: hidden;"></iframe>
<script type="text/javascript" id="" charset="">window.appier_q=window.appier_q||[];window.appier_q.push({t:"register",content:{id:"qkz5",site:"sc.com_hk"}},{action_id:"Ug6UbVmHCx9PEIO",track_id:"e0cWthuFXoytbBu",opts:{unique_key:"true"}},{t:"pv_track",action_id:"2cWZuu2GRQ1ogto",track_id:"e0cWthuFXoytbBu",isCountReload:!0,counter:0},{t:"pv_track",action_id:"lJNTxb5DnuhuFUj",track_id:"e0cWthuFXoytbBu",isCountReload:!1,counter:1});</script>
<script id="" text="" charset="" type="text/javascript" src="//jscdn.appier.net/aa.js?id=sc.com_hk"></script><script type="text/javascript" id="" charset="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","1682745115305829");fbq("track","PageView");fbq("trackCustom",{external_id:google_tag_manager["rm"]["8233097"](116)});</script><script type="text/javascript" id="" charset="">(function(d,a,b,f,e){d[e]=d[e]||[];d[e].push({projectId:"10000",properties:{pixelId:"406166"}});var c=a.createElement(b);c.src=f;c.async=!0;c.onload=c.onreadystatechange=function(){var a=this.readyState,c=d[e];if(!a||"complete"==a||"loaded"==a)try{var b=YAHOO.ywa.I13N.fireBeacon;d[e]=[];d[e].push=function(a){b([a])};b(c)}catch(g){}};a=a.getElementsByTagName(b)[0];b=a.parentNode;b.insertBefore(c,a)})(window,document,"script","https://s.yimg.com/wi/ytc.js","dotq");</script><script id="" text="" charset="" type="text/javascript" src="//jscdn.appier.net/aa.js?id=sc.com_hk"></script><script id="" text="" charset="" type="text/javascript" src="https://go.affec.tv/j/611b2b61737ce37c388dd38f?ver=Retail&amp;pnm=[product_name]&amp;pid=[product_id]&amp;pscat=[product_sub_cat_name]&amp;pscid=[product_sub_cat_id]&amp;pct=[product_category]&amp;cid=[product_category_id]&amp;rev=[revenue]&amp;cur=[currency]&amp;cpn=[voucher_code]&amp;url=[url]&amp;mem=[membership]&amp;oid=[order_id]&amp;qty=[quantity]&amp;custom1=[custom1]&amp;custom2=[custom2]&amp;custom3=[custom3]&amp;gdpr=[GDPR_APPLIES]&amp;gdpr_consent=[GDPR_TCF_CONSENT_STRING]"></script><script type="text/javascript" id="" charset="">window._tfa=window._tfa||[];window._tfa.push({notify:"event",name:"page_view",id:1626789});!function(a,b,d,c){document.getElementById(c)||(a.async=1,a.src=d,a.id=c,b.parentNode.insertBefore(a,b))}(document.createElement("script"),document.getElementsByTagName("script")[0],"//cdn.taboola.com/libtrc/unip/1626789/tfa.js","tb_tfa_script");</script>
<iframe height="0" width="0" src="https://6024809.fls.doubleclick.net/activityi;src=6024809;type=loanp0;cat=loanp0;ord=4779850564989;npa=0;auiddc=885611038.1742266178;u5=English;ps=1;pcor=2104494823;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-6024809/loanp0/loanp0+standard" data-load-time="1742266179309" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=6024809;type=loanp0;cat=loanp0;ord=4779850564989;npa=0;auiddc=885611038.1742266178;u5=English;ps=1;pcor=2104494823;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://6024809.fls.doubleclick.net/activityi;src=6024809;type=scbhk;cat=schkland;ord=3067546906411;npa=0;auiddc=885611038.1742266178;u12=%2Fhk%2Floans%2Fpersonal-instalment-loan%2F;u13=loans;u14=personal-instalment-loan;u15=personal-instalment-loan;u17=hk;u5=en;ps=1;pcor=875662814;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-6024809/scbhk/schkland+standard" data-load-time="1742266179312" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=6024809;type=scbhk;cat=schkland;ord=3067546906411;npa=0;auiddc=885611038.1742266178;u12=%2Fhk%2Floans%2Fpersonal-instalment-loan%2F;u13=loans;u14=personal-instalment-loan;u15=personal-instalment-loan;u17=hk;u5=en;ps=1;pcor=875662814;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://6024809.fls.doubleclick.net/activityi;src=6024809;type=loanp0;cat=loanp0;ord=8527426253783;npa=0;auiddc=885611038.1742266178;ps=1;pcor=927876319;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-6024809/loanp0/loanp0+standard" data-load-time="1742266179316" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=6024809;type=loanp0;cat=loanp0;ord=8527426253783;npa=0;auiddc=885611038.1742266178;ps=1;pcor=927876319;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://8005120.fls.doubleclick.net/activityi;src=8005120;type=invmedia;cat=leqwq78p;ord=1042881784964;npa=0;auiddc=885611038.1742266178;ps=1;pcor=667576528;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-8005120/invmedia/leqwq78p+standard" data-load-time="1742266179370" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=8005120;type=invmedia;cat=leqwq78p;ord=1042881784964;npa=0;auiddc=885611038.1742266178;ps=1;pcor=667576528;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://8744175.fls.doubleclick.net/activityi;src=8744175;type=invmedia;cat=pr2vkkjh;ord=7323506257027;npa=0;auiddc=885611038.1742266178;ps=1;pcor=697133460;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9190294465z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-8744175/invmedia/pr2vkkjh+standard" data-load-time="1742266179392" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=8744175;type=invmedia;cat=pr2vkkjh;ord=7323506257027;npa=0;auiddc=885611038.1742266178;ps=1;pcor=697133460;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9190294465z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://6629002.fls.doubleclick.net/activityi;src=6629002;type=invmedia;cat=hkcon0;ord=8597033441962;npa=0;auiddc=885611038.1742266178;u1=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F;u2=personal-instalment-loan;ps=1;pcor=541571736;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9189721130z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-6629002/invmedia/hkcon0+standard" data-load-time="1742266179490" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=6629002;type=invmedia;cat=hkcon0;ord=8597033441962;npa=0;auiddc=885611038.1742266178;u1=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F;u2=personal-instalment-loan;ps=1;pcor=541571736;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9189721130z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://9579696.fls.doubleclick.net/activityi;src=9579696;type=invmedia;cat=scb_l003;ord=9281155097632;npa=0;auiddc=885611038.1742266178;ps=1;pcor=359725891;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9190655833z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-9579696/invmedia/scb_l003+standard" data-load-time="1742266179512" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=9579696;type=invmedia;cat=scb_l003;ord=9281155097632;npa=0;auiddc=885611038.1742266178;ps=1;pcor=359725891;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9190655833z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://8134849.fls.doubleclick.net/activityi;src=8134849;type=glouni;cat=glolands;ord=9833321272883;npa=0;auiddc=885611038.1742266178;u1=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F;u10=en;u2=loans;u3=personal-instalment-loan;u9=hk;ps=1;pcor=2085072171;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9181629348z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-8134849/glouni/glolands+standard" data-load-time="1742266179535" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=8134849;type=glouni;cat=glolands;ord=9833321272883;npa=0;auiddc=885611038.1742266178;u1=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F;u10=en;u2=loans;u3=personal-instalment-loan;u9=hk;ps=1;pcor=2085072171;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9181629348z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><script id="" text="" charset="" type="text/javascript" src="https://p.teads.tv/teads-fellow.js"></script><div id="onetrust-consent-sdk"><div class="onetrust-pc-dark-filter ot-hide ot-fade-in"></div><div id="onetrust-banner-sdk" class="otFlat otRelFont bottom ot-wo-title vertical-align-content" tabindex="0" role="region" aria-label="Cookie banner" style="bottom: 0px;"><div role="alertdialog" aria-describedby="onetrust-policy-text" aria-label="Privacy"><div class="ot-sdk-container"><div class="ot-sdk-row"><div id="onetrust-group-container" class="ot-sdk-eight ot-sdk-columns ot-sdk-eleven"><div class="banner_logo"></div><div id="onetrust-policy"><p id="onetrust-policy-text">To enhance your experience, we use cookies and similar technologies. This enables us to optimise site functionality and to personalise your visit by remembering your choices, such as your preferred language, and by providing tailored ads in our own and third parties' online media. By continuing your visit on this website, you accept the use of cookies and similar technologies. For more details and information on how to manage your cookie settings, please read our<a href="https://www.sc.com/hk/cookie-policy/" aria-label="More information about your privacy">Cookie Policy.</a></p></div></div></div></div><!-- Close Button --><div id="onetrust-close-btn-container"><button class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon" style="background-image: url(&quot;https://av.sc.com/assets/tpl/onetrust/production/hk/consent/dcfcce45-805d-4309-a4b1-704b7638f2c9/301f5d62-0fe6-4311-af94-fbe234a827c4/logos/static/ot_close.svg&quot;);" aria-label="Close"></button></div><!-- Close Button END--></div></div><div id="onetrust-pc-sdk" class="otPcCenter ot-hide ot-fade-in otRelFont" lang="en" aria-label="Preference center" role="region"><div role="alertdialog" aria-modal="true" aria-describedby="ot-pc-desc" style="height: 100%;" aria-label="Privacy Preference Center"><!-- Close Button --><div class="ot-pc-header"><!-- Logo Tag --><div class="ot-pc-logo" role="img" aria-label="Company Logo"><img alt="Company Logo" src="https://av.sc.com/assets/tpl/onetrust/production/hk/consent/dcfcce45-805d-4309-a4b1-704b7638f2c9/301f5d62-0fe6-4311-af94-fbe234a827c4/logos/static/ot_company_logo.png"></div><button id="close-pc-btn-handler" class="ot-close-icon" aria-label="Close" style="background-image: url(&quot;https://av.sc.com/assets/tpl/onetrust/production/hk/consent/dcfcce45-805d-4309-a4b1-704b7638f2c9/301f5d62-0fe6-4311-af94-fbe234a827c4/logos/static/ot_close.svg&quot;);"></button></div><!-- Close Button --><div id="ot-pc-content" class="ot-pc-scrollbar"><div class="ot-optout-signal ot-hide"><div class="ot-optout-icon"><svg xmlns="http://www.w3.org/2000/svg"><path class="ot-floating-button__svg-fill" d="M14.588 0l.445.328c1.807 1.303 3.961 2.533 6.461 3.688 2.015.93 4.576 1.746 7.682 2.446 0 14.178-4.73 24.133-14.19 29.864l-.398.236C4.863 30.87 0 20.837 0 6.462c3.107-.7 5.668-1.516 7.682-2.446 2.709-1.251 5.01-2.59 6.906-4.016zm5.87 13.88a.75.75 0 00-.974.159l-5.475 6.625-3.005-2.997-.077-.067a.75.75 0 00-.983 1.13l4.172 4.16 6.525-7.895.06-.083a.75.75 0 00-.16-.973z" fill="#FFF" fill-rule="evenodd"></path></svg></div><span></span></div><h2 id="ot-pc-title">Privacy Preference Center</h2><div id="ot-pc-desc">When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.
            <br><a href="https://cookiepedia.co.uk/giving-consent-to-cookies" class="privacy-notice-link" rel="noopener" target="_blank" aria-label="More information about your privacy, opens in a new tab">More information</a></div><button id="accept-recommended-btn-handler">Allow All</button><section class="ot-sdk-row ot-cat-grp"><h3 id="ot-category-title"> Manage Consent Preferences</h3><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0002"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0002" aria-labelledby="ot-header-id-C0002"></button><!-- Accordion header --><div class="ot-acc-hdr ot-always-active-group"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0002">Performance cookies</h4><div class="ot-always-active">Always Active</div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0002">To create the best and most relevant experience for you, these cookies help us analyse and understand what areas need to be improved and refined.</p></div></div><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0001"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0001" aria-labelledby="ot-header-id-C0001"></button><!-- Accordion header --><div class="ot-acc-hdr ot-always-active-group"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0001">Strictly necessary cookies (Always on)</h4><div class="ot-always-active">Always Active</div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0001">Your security and privacy are our top priority, that’s why these cookies are always on to ensure the safest and smoothest online experience.</p></div></div><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0004"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0004" aria-labelledby="ot-header-id-C0004"></button><!-- Accordion header --><div class="ot-acc-hdr ot-always-active-group"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0004">Advertising cookies</h4><div class="ot-always-active">Always Active</div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0004">To make sure we only send what’s most relevant to your needs, these cookies help us and our partners understand what matters most to you. The data collected can be shared with third parties, such as advertisers or platforms, to create an ecosystem that is always relevant to you.</p></div></div><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0003"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0003" aria-labelledby="ot-header-id-C0003"></button><!-- Accordion header --><div class="ot-acc-hdr ot-always-active-group"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0003">Functionality cookies</h4><div class="ot-always-active">Always Active</div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0003">For your ease of use and convenience, these cookies remember the choices you made (e.g. language and region) and personalise our website to make it most relevant for you.</p></div></div><!-- Groups sections starts --><!-- Group section ends --><!-- Accordion Group section starts --><!-- Accordion Group section ends --></section></div><section id="ot-pc-lst" class="ot-hide ot-hosts-ui ot-pc-scrollbar"><div id="ot-pc-hdr"><div id="ot-lst-title"><button class="ot-link-btn back-btn-handler" aria-label="Back"><svg id="ot-back-arw" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 444.531 444.531" xml:space="preserve"><title>Back Button</title><g><path fill="#656565" d="M213.13,222.409L351.88,83.653c7.05-7.043,10.567-15.657,10.567-25.841c0-10.183-3.518-18.793-10.567-25.835
                    l-21.409-21.416C323.432,3.521,314.817,0,304.637,0s-18.791,3.521-25.841,10.561L92.649,196.425
                    c-7.044,7.043-10.566,15.656-10.566,25.841s3.521,18.791,10.566,25.837l186.146,185.864c7.05,7.043,15.66,10.564,25.841,10.564
                    s18.795-3.521,25.834-10.564l21.409-21.412c7.05-7.039,10.567-15.604,10.567-25.697c0-10.085-3.518-18.746-10.567-25.978
                    L213.13,222.409z"></path></g></svg></button><h3>Performance Cookies</h3></div><div class="ot-lst-subhdr"><div class="ot-search-cntr"><p role="status" class="ot-scrn-rdr"></p><label for="vendor-search-handler" class="ot-scrn-rdr"></label> <input id="vendor-search-handler" type="text" name="vendor-search-handler"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 -30 110 110" aria-hidden="true"><title>Search Icon</title><path fill="#2e3644" d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23
            s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92
            c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17
            s-17-7.626-17-17S14.61,6,23.984,6z"></path></svg></div><div class="ot-fltr-cntr"><button id="filter-btn-handler" aria-label="Filter" aria-haspopup="true"><svg role="presentation" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 402.577 402.577" xml:space="preserve"><title>Filter Icon</title><g><path fill="#fff" d="M400.858,11.427c-3.241-7.421-8.85-11.132-16.854-11.136H18.564c-7.993,0-13.61,3.715-16.846,11.136
      c-3.234,7.801-1.903,14.467,3.999,19.985l140.757,140.753v138.755c0,4.955,1.809,9.232,5.424,12.854l73.085,73.083
      c3.429,3.614,7.71,5.428,12.851,5.428c2.282,0,4.66-0.479,7.135-1.43c7.426-3.238,11.14-8.851,11.14-16.845V172.166L396.861,31.413
      C402.765,25.895,404.093,19.231,400.858,11.427z"></path></g></svg></button></div><div id="ot-anchor"></div><section id="ot-fltr-modal"><div id="ot-fltr-cnt"><button id="clear-filters-handler">Clear</button><div class="ot-fltr-scrlcnt ot-pc-scrollbar"><div class="ot-fltr-opts"><div class="ot-fltr-opt"><div class="ot-chkbox"><input id="chkbox-id" type="checkbox" aria-checked="false" class="category-filter-handler"> <label for="chkbox-id"><span class="ot-label-txt">checkbox label</span></label> <span class="ot-label-status">label</span></div></div></div><div class="ot-fltr-btns"><button id="filter-apply-handler">Apply</button> <button id="filter-cancel-handler">Cancel</button></div></div></div></section></div></div><section id="ot-lst-cnt" class="ot-host-cnt ot-pc-scrollbar"><div id="ot-sel-blk"><div class="ot-sel-all"><div class="ot-sel-all-hdr"><span class="ot-consent-hdr">Consent</span> <span class="ot-li-hdr">Leg.Interest</span></div><div class="ot-sel-all-chkbox"><div class="ot-chkbox" id="ot-selall-hostcntr"><input id="select-all-hosts-groups-handler" type="checkbox" aria-checked="false"> <label for="select-all-hosts-groups-handler"><span class="ot-label-txt">checkbox label</span></label> <span class="ot-label-status">label</span></div><div class="ot-chkbox" id="ot-selall-vencntr"><input id="select-all-vendor-groups-handler" type="checkbox" aria-checked="false"> <label for="select-all-vendor-groups-handler"><span class="ot-label-txt">checkbox label</span></label> <span class="ot-label-status">label</span></div><div class="ot-chkbox" id="ot-selall-licntr"><input id="select-all-vendor-leg-handler" type="checkbox" aria-checked="false"> <label for="select-all-vendor-leg-handler"><span class="ot-label-txt">checkbox label</span></label> <span class="ot-label-status">label</span></div></div></div></div><div class="ot-sdk-row"><div class="ot-sdk-column"></div></div></section></section><div class="ot-pc-footer"><div class="ot-btn-container"><button class="ot-pc-refuse-all-handler">Reject All</button> <button class="save-preference-btn-handler onetrust-close-btn-handler">Confirm My Choices</button></div><!-- Footer logo --><div class="ot-pc-footer-logo"><a href="https://www.onetrust.com/products/cookie-consent/" target="_blank" rel="noopener noreferrer" aria-label="Powered by OneTrust Opens in a new Tab"><img alt="Powered by Onetrust" src="https://av.sc.com/assets/tpl/onetrust/production/hk/consent/dcfcce45-805d-4309-a4b1-704b7638f2c9/301f5d62-0fe6-4311-af94-fbe234a827c4/logos/static/powered_by_logo.svg" title="Powered by OneTrust Opens in a new Tab"></a></div></div><!-- Cookie subgroup container --><!-- Vendor list link --><!-- Cookie lost link --><!-- Toggle HTML element --><!-- Checkbox HTML --><!-- plus minus--><!-- Arrow SVG element --><!-- Accordion basic element --><span class="ot-scrn-rdr" aria-atomic="true" aria-live="polite"></span><!-- Vendor Service container and item template --></div><iframe class="ot-text-resize" title="onetrust-text-resize" style="position: absolute; top: -50000px; width: 100em;" aria-hidden="true"></iframe></div><div id="ot-sdk-btn-floating" title="Cookies Settings" class="ot-floating-button ot-hide"><div class="ot-floating-button__front custom-persistent-icon"><button type="button" class="ot-floating-button__open" aria-label="Open Preferences"></button></div><div class="ot-floating-button__back custom-persistent-icon"><button type="button" class="ot-floating-button__close" aria-label="Close Preferences" aria-hidden="true"><!--?xml version="1.0" encoding="UTF-8"?--> <svg role="presentation" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="Banner_02" class="ot-floating-button__svg-fill" transform="translate(-318.000000, -725.000000)" fill="#ffffff" fill-rule="nonzero"><g id="Group-2" transform="translate(305.000000, 712.000000)"><g id="icon/16px/white/close"><polygon id="Line1" points="13.3333333 14.9176256 35.0823744 36.6666667 36.6666667 35.0823744 14.9176256 13.3333333"></polygon><polygon id="Line2" transform="translate(25.000000, 25.000000) scale(-1, 1) translate(-25.000000, -25.000000) " points="13.3333333 14.9176256 35.0823744 36.6666667 36.6666667 35.0823744 14.9176256 13.3333333"></polygon></g></g></g></g></svg></button></div></div></div><script type="text/javascript" src="https://secure.adnxs.com/px?gdpr=[GDPR_APPLIES]&amp;gdpr_consent=[GDPR_TCF_CONSENT_STRING]&amp;id=1510833&amp;order_id=[order_id]&amp;seg=27387092&amp;t=1&amp;value="></script><script type="text/javascript" src="https://insight.adsrvr.org/track/pxl/?adv=i6zlgrf&amp;ct=0%3Awkk35re&amp;fmt=3&amp;gdpr=[GDPR_APPLIES]&amp;gdpr_consent=[GDPR_TCF_CONSENT_STRING]"></script><img width="1" height="1" src="https://map.go.affec.tv/map/af/?gdpr=[GDPR_APPLIES]&amp;gdpr_consent=[GDPR_TCF_CONSENT_STRING]" style="display: none;">
<script type="text/javascript" id="" charset="">window.teads_e=window.teads_e||[];window.teads_buyer_pixel_id=8962;</script><img class="ywa-10000" src="https://sp.analytics.yahoo.com/sp.pl?a=10000&amp;d=Tue%2C%2018%20Mar%202025%2002%3A49%3A40%20GMT&amp;n=-8&amp;b=Personal%20Instalment%20Loan%20%7C%20Interest%20rate%20as%20low%20as%201.85%25%20%7C%20Hong%20Kong%20%E2%80%93%20Standard%20Chartered%20HK&amp;.yp=406166&amp;f=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F&amp;enc=UTF-8&amp;yv=1.16.6&amp;tagmgr=gtm%2Cadobe" alt="dot image pixel" style="display: none;">
  <script type="text/javascript" id="" charset="">var _qevents=_qevents||[];(function(){var a=document.createElement("script");a.src=("https:"==document.location.protocol?"https://secure":"http://edge")+".quantserve.com/quant.js";a.async=!0;a.type="text/javascript";var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b)})();_qevents.push({qacct:"p-Mp998fWY2NSrV"});</script>
 <iframe height="0" width="0" src="https://6024809.fls.doubleclick.net/activityi;src=6024809;type=loanp0;cat=loanp0;ord=3195185700346;npa=0;auiddc=885611038.1742266178;u5=en;ps=1;pcor=1424403760;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-6024809/loanp0/loanp0+standard" data-load-time="1742266185589" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=6024809;type=loanp0;cat=loanp0;ord=3195185700346;npa=0;auiddc=885611038.1742266178;u5=en;ps=1;pcor=1424403760;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9137486422z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719~102887800;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe height="0" width="0" src="https://9579696.fls.doubleclick.net/activityi;src=9579696;type=invmedia;cat=scb_l022;ord=1181452804499;npa=0;auiddc=885611038.1742266178;ps=1;pcor=209858987;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9190655833z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=1;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><iframe allow="join-ad-interest-group" data-tagging-id="DC-9579696/invmedia/scb_l022+standard" data-load-time="1742266185608" height="0" width="0" src="https://td.doubleclick.net/td/fls/rul/activityi;fledge=1;src=9579696;type=invmedia;cat=scb_l022;ord=1181452804499;npa=0;auiddc=885611038.1742266178;ps=1;pcor=209858987;uaa=x86;uab=64;uafvl=HeadlessChrome%3B131.0.6778.33%7CChromium%3B131.0.6778.33%7CNot_A%2520Brand%3B24.0.0.0;uamb=0;uam=;uap=Windows;uapv=19.0.0;uaw=0;pscdl=noapi;frm=0;_tu=Kg;gtm=45fe53d3v9190655833z878233097za201zb78233097;gcd=13l3l3l3l1l1;dma=0;dc_fmt=9;tag_exp=102482433~102587591~102717422~102788824~102813109~102814060~102825837~102879719;epver=2;~oref=https%3A%2F%2Fwww.sc.com%2Fhk%2Floans%2Fpersonal-instalment-loan%2F?" style="display: none; visibility: hidden;"></iframe><script id="" text="" charset="" type="text/javascript" src="https://js.adsrvr.org/up_loader.1.1.0.js"></script></body></html>