window.cxs && window.cxs.setOptions({ prefix: "c2-" });
window.wsb=window.wsb||{};window.wsb["Theme27"]=window.wsb["Theme27"]||window.radpack("@widget/LAYOUT/bs-layout27-Theme-publish-Theme").then(function(t){return new t.default();});
window.wsb["FreemiumAd"]=function(e){let{adEndpoint:t,isPublish:a,containerId:o}=e;const r=1e4,l=/<script[^>]*>([\s\S]*)<\/script>/;let n,i,s;function c(e){e.preventDefault(),e.stopPropagation();const t=new CustomEvent("editor",{detail:{type:"showModal",modal:"plans",source:"freemiumAd"}});window.dispatchEvent(t)}function g(e){if(s=document.getElementById(o),!s)return;n=document.createElement("div"),n.style.cssText="width:100%;",s.prepend(n),i=document.createElement("div"),i.setAttribute("data-freemium-ad",!0),i.style.cssText=`overflow:hidden;width:100%;z-index:${r};position:fixed;left:0;`,i.innerHTML=(e||"").replace(l,""),s.prepend(i);const t=`${i.offsetHeight}px`;if(n.style.minHeight=t,window.requestAnimationFrame((()=>{const e=document.querySelector("[data-stickynav]");e&&"fixed"===e.style.position&&(e.style.top=t)})),a){const t=l.exec(e);if(t){const e=document.createElement("script");e.appendChild(document.createTextNode(t[1])),document.head.appendChild(e)}}else i.addEventListener("click",c,{useCapture:!0})}return function(){const e=a&&sessionStorage.getItem(t)||"";e?g(e):window.fetch(t).then((e=>e.ok&&e.text())).then((e=>{e&&(sessionStorage.setItem(t,e),g(e))})).catch((()=>{}))}(),function(){!a&&i.removeEventListener("click",c,{useCapture:!0}),s&&(s.removeChild(n),s.removeChild(i))}};
window.wsb["FreemiumAd"](JSON.parse("{\"adEndpoint\":\"/markup/ad\",\"isPublish\":true,\"containerId\":\"freemium-ad-22093\"}"));
window.wsb["DynamicFontScaler"]=function(t){let e,{containerId:n,targetId:o,fontSizes:r,maxLines:i,prioritizeDefault:s}=t;if("undefined"==typeof document)return;const a=document.getElementById(n),c=document.getElementById(o);function l(t){return function(t){const e=parseInt(y(t,"padding-left")||0,10),n=parseInt(y(t,"padding-right")||0,10);return t.scrollWidth+e+n}(t)<=a.clientWidth&&function(t){const e=t.offsetHeight,n=parseInt(y(t,"line-height"),10)||1;return Math.floor(e/n)}(t)<=i}function p(t){return parseInt(y(t,"font-size")||0,10)}function d(t){if(1===t.length)return t[0];const e=t.filter(l);if(1===e.length)return e[0];if(!e.length)return function(t){return t.sort(((t,e)=>p(t)-p(e)))[0]}(t);return e.sort(((t,e)=>p(e)-p(t)))[0]}function u(){if(!a||!c||e===window.innerWidth)return;if(c.hasAttribute("data-font-scaled"))return void g();e=window.innerWidth;const t=Array.prototype.slice.call(a.querySelectorAll(`[data-scaler-id="scaler-${n}"]`)).sort(((t,e)=>r.indexOf(t.getAttribute("data-size"))-r.indexOf(e.getAttribute("data-size"))));if(a.clientWidth&&t.length){const e=a.style.width||"";a.style.width="100%",t.forEach((t=>{t.style.display="inline-block",t.style.maxWidth=`${a.clientWidth}px`}));const n=d(t);!function(t){t.forEach((t=>{t.style.display="none",t.style.maxWidth=""}))}(t),a.style.width=e;const r=y(n,"font-size"),i=c.getAttribute("data-last-size");if(r&&r!==i){if(s){const t=y(c,"font-size");if(parseInt(r,10)>=parseInt(t,10))return}c.setAttribute("data-last-size",r);let t=document.querySelector(`#${o}-style`);t||(t=document.createElement("style"),t.id=`${o}-style`,document.head.appendChild(t)),t.textContent=`#${c.id} { font-size: ${r} !important; }`}}}function g(){c&&c.removeAttribute("data-last-size");const t=document.querySelector(`#${o}-style`);t&&t.parentNode.removeChild(t)}function y(t,e){return document.defaultView.getComputedStyle(t).getPropertyValue(e)}return u(),window.addEventListener("resize",u),()=>{g(),window.removeEventListener("resize",u)}};
window.wsb["DynamicFontScaler"](JSON.parse("{\"containerId\":\"logo-container-22096\",\"targetId\":\"logo-text-22097\",\"fontSizes\":[\"xxlarge\",\"xlarge\",\"large\"],\"maxLines\":1,\"prioritizeDefault\":false}"));
window.wsb["DynamicFontScaler"](JSON.parse("{\"containerId\":\"logo-container-22099\",\"targetId\":\"logo-text-22100\",\"fontSizes\":[\"xxlarge\",\"xlarge\",\"large\"],\"maxLines\":3,\"prioritizeDefault\":false}"));
window.wsb["DynamicFontScaler"](JSON.parse("{\"containerId\":\"tagline-container-22101\",\"targetId\":\"dynamic-tagline-22102\",\"fontSizes\":[\"xxlarge\",\"xlarge\",\"large\"],\"maxLines\":4}"));
window.wsb['context-bs-1']=JSON.parse("{\"env\":\"production\",\"renderMode\":\"PUBLISH\",\"fonts\":[\"righteous\",\"josefin-sans\",\"great-vibes\"],\"colors\":[\"#f5d8d0\"],\"fontScale\":\"medium\",\"locale\":\"en-IN\",\"language\":\"en\",\"resellerId\":1,\"internalLinks\":{\"11540997-2db4-4e3d-8261-0a944d95c6ad\":{\"pageId\":\"5b1964fc-96a0-4a42-962d-17657b6bcf79\",\"routePath\":\"/\"}},\"isHomepage\":true,\"navigationMap\":{\"4010c8c1-b008-4b7d-8303-725fc3a5f5b0\":{\"isFlyoutMenu\":false,\"active\":false,\"pageId\":\"4010c8c1-b008-4b7d-8303-725fc3a5f5b0\",\"name\":\"404\",\"href\":\"/404\",\"target\":\"\",\"visible\":false,\"requiresAuth\":false,\"tags\":[\"404\"],\"rel\":\"\",\"type\":\"page\",\"showInFooter\":false},\"5b1964fc-96a0-4a42-962d-17657b6bcf79\":{\"isFlyoutMenu\":false,\"active\":true,\"pageId\":\"5b1964fc-96a0-4a42-962d-17657b6bcf79\",\"name\":\"Home\",\"href\":\"/\",\"target\":\"\",\"visible\":true,\"requiresAuth\":false,\"tags\":[],\"rel\":\"\",\"type\":\"page\",\"showInFooter\":false}},\"dials\":{\"colors\":[{\"id\":\"#f5d8d0\",\"meta\":{\"primary\":\"rgb(245, 216, 208)\",\"accent\":\"rgb(17, 17, 17)\",\"neutral\":\"rgb(255, 255, 255)\"}}],\"fonts\":{\"primary\":{\"id\":\"righteous\",\"description\":\"\",\"tags\":[],\"meta\":{\"order\":33,\"primary\":{\"id\":\"righteous\",\"name\":\"Righteous\",\"url\":\"//fonts.googleapis.com/css?family=Righteous:400&display=swap\",\"family\":\"'Righteous', serif, system-ui\",\"size\":14,\"weight\":400,\"weights\":[400,700],\"styles\":{\"letterSpacing\":\"4px\"}},\"alternate\":{\"id\":\"josefin-sans\",\"name\":\"Josefin Sans\",\"url\":\"//fonts.googleapis.com/css?family=Josefin+Sans:400,600,700&display=swap\",\"family\":\"'Josefin Sans', Arial, sans-serif\",\"size\":16,\"weight\":400,\"weights\":[400,600,700],\"styles\":{\"letterSpacing\":\"normal\",\"textTransform\":\"none\"}}},\"overridesAlternate\":[{\"locales\":[\"vi-VN\"],\"meta\":{\"alternate\":{\"family\":\"Arial, sans-serif\"}}},{\"locales\":[\"ja-JP\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, Meiryo, '\u30E1\u30A4\u30EA\u30AA', sans-serif\"}}},{\"locales\":[\"ko-KR\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, '\uAD74\uB9BC', Gulim, '\uAD74\uB9BC\uCCB4', GulimChe, sans-serif\"}}},{\"locales\":[\"th-TH\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, BrowalliaUPC, Tahoma, sans-serif\"}}},{\"locales\":[\"zh-CN\",\"zh-SG\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, '\u4E2D\u6613\u9ED1\u4F53', SimHei, sans-serif\"}}},{\"locales\":[\"zh-HK\",\"zh-TW\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Slab, '\u5FAE\u8EDF\u6B63\u9ED1\u9AD4', Microsoft JhengHei, sans-serif\"}}}],\"overridesPrimary\":[{\"languages\":[\"en\"],\"meta\":{\"primary\":{\"styles\":{\"textTransform\":\"uppercase\"}}}}]},\"alternate\":{\"id\":\"josefin-sans\",\"description\":\"\",\"tags\":[],\"meta\":{\"order\":7,\"alternate\":{\"id\":\"josefin-sans\",\"name\":\"Josefin Sans\",\"url\":\"//fonts.googleapis.com/css?family=Josefin+Sans:400,600,700&display=swap\",\"family\":\"'Josefin Sans', Arial, sans-serif\",\"size\":16,\"weight\":400,\"weights\":[400,600,700],\"styles\":{\"letterSpacing\":\"normal\",\"textTransform\":\"none\"}}},\"overridesAlternate\":[{\"locales\":[\"vi-VN\"],\"meta\":{\"alternate\":{\"family\":\"Arial, sans-serif\"}}},{\"locales\":[\"ja-JP\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, Meiryo, '\u30E1\u30A4\u30EA\u30AA', sans-serif\"}}},{\"locales\":[\"ko-KR\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, '\uAD74\uB9BC', Gulim, '\uAD74\uB9BC\uCCB4', GulimChe, sans-serif\"}}},{\"locales\":[\"th-TH\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, BrowalliaUPC, Tahoma, sans-serif\"}}},{\"locales\":[\"zh-CN\",\"zh-SG\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Sans, '\u4E2D\u6613\u9ED1\u4F53', SimHei, sans-serif\"}}},{\"locales\":[\"zh-HK\",\"zh-TW\"],\"meta\":{\"alternate\":{\"family\":\"Josefin Slab, '\u5FAE\u8EDF\u6B63\u9ED1\u9AD4', Microsoft JhengHei, sans-serif\"}}}]},\"logo\":{\"id\":\"great-vibes\",\"description\":\"\",\"tags\":[\"casual\",\"fun\"],\"meta\":{\"order\":14,\"logo\":{\"id\":\"great-vibes\",\"name\":\"Great Vibes\",\"url\":\"//fonts.googleapis.com/css?family=Great+Vibes&display=swap\",\"family\":\"'Great Vibes', Georgia, serif, system-ui\",\"size\":19,\"weight\":400,\"weights\":[400,700],\"styles\":{\"textTransform\":\"none\",\"fontSize\":\"xxlarge\",\"fontWeight\":400,\"letterSpacing\":\"0\"}}}}}},\"theme\":\"Theme27\"}");
Core.utils.deferBootstrap({elId:'bs-1',componentName:'@widget/GALLERY/bs-gallery4-Gallery',props:JSON.parse("{\"upgradeable\":false,\"preset\":\"gallery4\",\"id\":\"fb7fb98d-adbd-4342-b65b-f1b77f505ece\",\"viewDevice\":null,\"staticContent\":{\"showMore\":\"Show More\",\"demoCaption1\":\"Use captions to provide more information about your photos\",\"demoCaption2\":\"Captions can prompt viewers to act. You can even insert a link\",\"demoCaption3\":\"Use the caption to call out things the viewer may not notice\",\"showLess\":\"Show Less\"},\"enableImageDimension\":true,\"galleryImages\":[[{\"image\":{\"hasAlpha\":false,\"width\":\"NaN%\",\"left\":\"NaN%\",\"height\":\"NaN%\",\"position\":\"50% 50%\",\"editedAspectRatio\":\"1\",\"imageDimension\":null,\"overlayAlpha\":0,\"colors\":[{\"hex\":\"#f4fafc\",\"rgb\":[244,250,252],\"hsluv\":[213.55485549880197,43.52694753923979,97.54919857067844],\"distance\":97.54919857067844},{\"hex\":\"#dff1f3\",\"rgb\":[223,241,243],\"hsluv\":[200.48317884501728,29.259243632684733,93.58841526995437],\"distance\":97.07123735223678},{\"hex\":\"#e7f0f2\",\"rgb\":[231,240,242],\"hsluv\":[207.48031501241522,20.61492682793267,93.86700318922564],\"distance\":96.50483008038672},{\"hex\":\"#8edbd9\",\"rgb\":[142,219,217],\"hsluv\":[189.68351784357282,56.4919023253529,82.3161873367264],\"distance\":88.49227622993828},{\"hex\":\"#50d2d5\",\"rgb\":[80,210,213],\"hsluv\":[194.8926170458302,85.1737083523088,77.36495744279753],\"distance\":86.42369665871128},{\"hex\":\"#26b0b2\",\"rgb\":[38,176,178],\"hsluv\":[194.13731292578566,94.56886559595098,65.25982301770333],\"distance\":75.25597989098117},{\"hex\":\"#66ab96\",\"rgb\":[102,171,150],\"hsluv\":[162.77386457596728,60.09566331681574,64.84958235814698],\"distance\":71.31129831365068},{\"hex\":\"#50a68a\",\"rgb\":[80,166,138],\"hsluv\":[159.03297707568618,72.95065909978524,62.12377813401112],\"distance\":69.86060231364432},{\"hex\":\"#7ea488\",\"rgb\":[126,164,136],\"hsluv\":[137.52176186057866,33.43844375945476,63.73964003592583],\"distance\":67.46548930592846},{\"hex\":\"#555954\",\"rgb\":[85,89,84],\"hsluv\":[120.33739877151156,7.421185183156963,37.1842822763717],\"distance\":38.26067134683048},{\"hex\":\"#272b27\",\"rgb\":[39,43,39],\"hsluv\":[127.71501294922363,10.187074647065602,16.938076908857084],\"distance\":18.3115482984226},{\"hex\":\"#1a1a16\",\"rgb\":[26,26,22],\"hsluv\":[85.8743202181635,18.405022820572523,9.075901442389814],\"distance\":11.154943502830854}],\"top\":\"NaN%\",\"oHeight\":836,\"fullWidth\":false,\"oWidth\":1255,\"filter\":\"NONE\",\"image\":\"//img1.wsimg.com/isteam/stock/6QJad5e\",\"coordinates\":{\"x\":null,\"y\":null},\"rotation\":\"0\",\"index\":0}},{\"image\":{\"oHeight\":1440,\"oWidth\":1769,\"image\":\"//img1.wsimg.com/isteam/stock/upmAxdd9ppFmZ3Aro\",\"index\":1}},{\"image\":{\"oHeight\":836,\"oWidth\":1254,\"image\":\"//img1.wsimg.com/isteam/stock/xrWr47W\",\"index\":2}},{\"image\":{\"oHeight\":1440,\"oWidth\":2160,\"image\":\"//img1.wsimg.com/isteam/stock/u0pQ50kl7DtzbpK93\",\"index\":3}},{\"image\":{\"oHeight\":887,\"oWidth\":1183,\"image\":\"//img1.wsimg.com/isteam/stock/y6lZ9mB\",\"index\":4}},{\"image\":{\"oHeight\":1440,\"oWidth\":2160,\"image\":\"//img1.wsimg.com/isteam/stock/u6yJZ2V5RKf8kGJbE\",\"index\":5}}]],\"renderAsThumbnail\":false,\"imageCount\":6,\"widgetId\":\"fb7fb98d-adbd-4342-b65b-f1b77f505ece\",\"section\":\"default\",\"category\":\"neutral\",\"locale\":\"en-IN\",\"env\":\"production\",\"renderMode\":\"PUBLISH\"}"),context:JSON.parse("{\"order\":1,\"widgetId\":\"fb7fb98d-adbd-4342-b65b-f1b77f505ece\",\"widgetType\":\"GALLERY\",\"widgetPreset\":\"gallery4\",\"group\":\"Section\",\"groupType\":\"Default\",\"section\":\"default\",\"category\":\"neutral\",\"fontSize\":\"medium\",\"fontFamily\":\"alternate\",\"websiteThemeOverrides\":{},\"widgetThemeOverrides\":{\"HeadingBeta\":{\"byType\":{\"SectionHeading\":{\"value\":{\"typography\":\"HeadingEpsilon\",\"featured\":false,\"style\":{\"fontSize\":\"large\"},\"fullWidth\":false}}}}}}"),contextKey:'context-bs-1',radpack:"@widget/GALLERY/bs-gallery4-Gallery"},false);
Core.utils.deferBootstrap({elId:'bs-2',componentName:'@widget/REVIEWS/bs-Component',props:JSON.parse("{\"hasBgImage\":true,\"upgradeable\":false,\"preset\":\"reviews1\",\"id\":\"d6dc9420-a365-4f82-aa7d-0859a554f71a\",\"planType\":\"commerce\",\"market\":\"en-IN\",\"publishDate\":\"2024-03-26T15:37:59.751Z\",\"fbPageId\":null,\"gmbShowPendingMessage\":false,\"publishAfterLastUpgrade\":false,\"providerType\":\"facebook\",\"isInternalPage\":false,\"isReseller\":false,\"accountId\":\"31140279-eb74-11ee-8342-3417ebe725e0\",\"viewDevice\":null,\"sectionTitle\":\"Blogs\",\"background\":{\"image\":\"//img1.wsimg.com/isteam/stock/ujaxO8DRbBHWjqA26\"},\"staticContent\":{\"txtPendingValidation\":\"Pending Validation\",\"reviewTitle\":\"Title\",\"add\":\"Add\",\"doesNotRecommend\":\"Doesn't recommend\",\"noWrittenReviews\":\"This customer did not write a review.\",\"connectionSuccess\":\"Successfully Connected!\",\"cantConnect\":\"Why can't I connect yet?\",\"reviewDate\":\"Review Date\",\"productReview\":\"{totalReviews} Product Review\",\"viewAllProductReviews\":\"View All {totalReviews} Product Reviews\",\"upgradeMessage\":\"Your site needs to have an online store to use {provider} reviews\",\"productReviews\":\"{totalReviews} Product Reviews\",\"goToProduct\":\"Go to {productName}\",\"anonymous\":\"Anonymous\",\"gmb3Days\":\"It may take up to 3 days to validate your business. Until then, reviews will not appear on your site.\",\"noReviewsYet\":\"There are no reviews yet.\",\"reviewerName\":\"Reviewer Name\",\"basedOn\":\"Based on the opinion of {reviewCount} people\",\"photo\":\"Photo\",\"gmbAwaitingData\":\"We are waiting for data. Please check back later\",\"reviewLink\":\"Review Link\",\"basedOnOne\":\"Based on the opinion of 1 person\",\"gmbUnderReview\":\"Google is reviewing your business info. We'll let you know when your listing is live.\",\"gmbPublishMessage\":\"Your website needs to be published before connecting to Google My Business.\",\"sourceMsgStatic\":\"Add reviews manually\",\"manualReviews\":\"Reviews\",\"ratingNone\":\"None\",\"reviewRating\":\"Rating\",\"percentRecommend\":\"{percent} recommend\",\"connectMsg\":\"To show reviews on your site, connect your account to {provider}\",\"twentyFourHourLag\":\"Data may take up to 24 hours to display.\",\"recommends\":\"Recommends\",\"reviewFirst\":\"Be the first to leave a review\",\"review\":\"{totalReviews} Review\",\"publishMessage\":\"Your website needs to be published before connecting to {provider}\",\"sourceMsgDynamic\":\"Connect to external source\",\"reviewBody\":\"Review\",\"upgradeNow\":\"Add Store Now\",\"viewMore\":\"View More\",\"reviews\":\"{totalReviews} Reviews\",\"cantConnectMsg\":\"Your website needs to be published before connecting to {provider}\",\"comingSoon\":\"Reviews coming soon!\",\"readFullReview\":\"Read full review\",\"labelForDeleteManualReview\":\"Delete Review\",\"gmbNoReviews\":\"You are successfully connected but there are no reviews yet.\",\"connectBtnText\":\"Connect to {provider}\",\"viewAllReviews\":\"View All {totalReviews} Reviews\"},\"websiteId\":\"1e210ddf-6d7a-440a-8a60-46eaf8fb9f99\",\"sourceType\":\"static\",\"manualReviews\":[{\"photo\":{},\"title\":\"Title 1\",\"body\":\"Review 1\",\"rating\":\"0\",\"name\":\"Anonymous\",\"date\":\"26/3/2024\"},{\"photo\":{},\"title\":\"Title 2\",\"body\":\"Review 2\",\"rating\":\"0\",\"name\":\"Anonymous\",\"date\":\"26/3/2024\"},{\"photo\":{},\"title\":\"Title 3\",\"body\":\"Review 3\",\"rating\":\"0\",\"name\":\"Anonymous\",\"date\":\"26/3/2024\"}],\"widgetId\":\"d6dc9420-a365-4f82-aa7d-0859a554f71a\",\"section\":\"default\",\"category\":\"neutral\",\"locale\":\"en-IN\",\"env\":\"production\",\"renderMode\":\"PUBLISH\"}"),context:JSON.parse("{\"order\":3,\"widgetId\":\"d6dc9420-a365-4f82-aa7d-0859a554f71a\",\"widgetType\":\"REVIEWS\",\"widgetPreset\":\"reviews1\",\"group\":\"Section\",\"groupType\":\"Banner\",\"section\":\"default\",\"category\":\"neutral\",\"fontSize\":\"medium\",\"fontFamily\":\"alternate\",\"websiteThemeOverrides\":{},\"widgetThemeOverrides\":{\"HeadingGamma\":{\"byType\":{\"SectionHeading\":{\"value\":{\"style\":{\"fontSize\":\"xxlarge\"},\"fullWidth\":false}}}}}}"),contextKey:'context-bs-1',radpack:"@widget/REVIEWS/bs-Component"},false);
window.wsb["CookieBannerScript"]=function(e){let{id:t,acceptCookie:o,dismissCookie:a}=e;const n=864e5;let i,l,r;function s(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:60;const o=new Date;o.setTime(o.getTime()+n*t);const a=`expires=${o.toUTCString()}`;document.cookie=`${e}=true;${a};path=/`}function c(e){return document.cookie.includes(e)}function p(){l&&l.removeEventListener("click",g),r&&r.removeEventListener("click",d),i.style.display="none"}function g(e){e.preventDefault(),u(),s(a),s(o),p()}function d(e){var t;e.preventDefault(),s(a),c(o)&&(t=o,document.cookie=`${t}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`),p()}function u(){window._allowCT=!0,window._allowCTListener&&window._allowCTListener.forEach((e=>e()))}c(o)?u():c(a)||setTimeout((()=>{i=document.getElementById(`${t}-banner`),l=document.getElementById(`${t}-accept`),r=document.getElementById(`${t}-decline`),l&&l.addEventListener("click",g),r&&r.addEventListener("click",d),i.style.transform="translateY(-500px)"}),200)};
window.wsb["CookieBannerScript"](JSON.parse("{\"id\":\"739e1199-ab84-47a1-ab94-331ae5ccb45c\",\"dismissCookie\":\"cookie_warning_dismissed\",\"acceptCookie\":\"cookie_terms_accepted\"}"));
Core.utils.renderBootstrap({elId:'bs-3',componentName:'@widget/MESSAGING/bs-Component',props:JSON.parse("{\"config\":{\"formSubmitEndpoint\":\"/messaging\",\"assetsHost\":\"https://img1.wsimg.com\",\"assetsBasePath\":\"/isteam\",\"contactsHost\":\"https://contacts.godaddy.com\",\"conversationsWebHost\":\"https://conversations.godaddy.com\",\"formSubmitHost\":\"https://contact.apps-api.instantpage.secureserver.net\",\"generateUrlHost\":\"https://url-generator.apps.secureserver.net\",\"vNextApiHost\":\"https://websites.api.godaddy.com\",\"reamazeApiHost\":\"https://{{websiteId}}reamaze.godaddy.com\",\"reamazeJsSource\":\"https://cdn.reamaze.com/assets/reamaze-loader.js\",\"reamazeCookieJsSource\":\"https://cdn.reamaze.com/assets/reamaze-godaddy-loader.js\"},\"businessName\":\"Nitin Gokarn\",\"reamazeBrandId\":\"1e210ddf-6d7a-440a-8a60-46eaf8fb9f99\",\"welcomeMessage\":\"Hi! Let us know how we can help and we\u2019ll respond shortly.\",\"formSuccessMessage\":\"Thanks for the message. We'll get back to you as soon as we can.\",\"emailOptInMessage\":\"Sign up to receive email updates, announcements, and more.\",\"emailOptInEnabled\":false,\"domainName\":\"nitingokarn.godaddysites.com\",\"cookieBannerEnabled\":true,\"formFields\":[{\"keyName\":\"name\",\"type\":\"SINGLE_LINE\",\"label\":\"Name\",\"validation\":\"required\",\"required\":true},{\"keyName\":\"phone\",\"type\":\"PHONE\",\"label\":\"Mobile\",\"validation\":\"phone\",\"required\":true},{\"keyName\":\"email\",\"type\":\"EMAIL\",\"label\":\"Email\",\"validation\":\"email\",\"required\":true,\"replyTo\":true},{\"keyName\":\"message\",\"type\":\"MULTI_LINE\",\"label\":\"How can we help?\",\"validation\":\"required\",\"required\":true},{\"type\":\"SUBMIT\",\"label\":\"Send\"}],\"accountId\":\"31140279-eb74-11ee-8342-3417ebe725e0\",\"websiteId\":\"1e210ddf-6d7a-440a-8a60-46eaf8fb9f99\",\"id\":\"822d5ae4-91d2-4f47-8375-11fe8d781bc4\",\"staticContent\":{\"submitButtonLoadingLabel\":\"Sending\",\"infoStartTitle\":\"Conversations\",\"contactFormResponseErrorMessage\":\"Something went wrong while sending your message, please try again later\",\"infoStartDesc\":\"Respond smarter and faster to website messages, text messages and Facebook Messenger. Receive instant notifications, reply from anywhere, all from your phone.\",\"infoStartTag\":\"New\",\"phoneValidationErrorMessage\":\"Please enter a valid phone number.\",\"defaultCancelButtonLabel\":\"Cancel\",\"contactsLinkInfoMessaging\":\"Contacts from your website messaging form are captured in Connections.\",\"defaultSubmitButtonLabel\":\"Send\",\"endOfChat\":\"end of chat\",\"infoConnectedDesc\":\"You are connected to the Conversations mobile app and are currently receiving all website messages there.\",\"infoRecommendedTag\":\"Recommended\",\"infoStartLink\":\"Get Started\",\"phoneUsOnlyValidationErrorMessage\":\"Please enter a valid U.S. mobile phone number.\",\"infoIncludedTag\":\"Included\",\"infoPublishRequiredDesc\":\"A publish is needed in order to complete this first step of enabling this feature.\",\"infoPendingLoginDesc\":\"A text message has been sent to you to download the Conversations app. Please download and install to complete set up.\",\"termsOfSerivce\":\"Terms of Service\",\"infoUnavailableDesc\":\"We currently only allow this to work with one website. To use this feature on this website, please disconnect from the active one.\",\"recaptchaDisclosure\":\"This site is protected by reCAPTCHA and the Google {privacyPolicy} and {termsOfSerivce} apply.\",\"emailValidationErrorMessage\":\"Please enter a valid email address.\",\"privacyPolicyURL\":\"https://policies.google.com/privacy\",\"infoUnavailableTitle\":\"Conversations\",\"requiredValidationErrorMessage\":\"Please fill in this required field\",\"infoUnavailableTag\":\"Unavailable\",\"contactsLinkText\":\"Manage my contacts\",\"privacyPolicy\":\"Privacy Policy\",\"infoPublishRequiredLink\":\"Publish Now\",\"infoPendingLoginLink\":\"Resend Link\",\"infoConnectedTitle\":\"Conversations Mobile App\",\"termsOfSerivceURL\":\"https://policies.google.com/terms\",\"messagesRatesLegalDisclosure\":\"By submitting your phone number, you agree to receive text messages from us. Message/ data rates may apply.\",\"emailMaxCountValidationErrorMessage\":\"Your email address is too long\",\"infoConnectedTag\":\"Connected\"},\"emailConfirmationMessage\":\"We've sent you a confirmation email, please click the link to verify your address.\",\"recaptchaType\":\"V3\",\"isMobile\":null,\"notificationPreference\":\"EMAIL\",\"isReseller\":false,\"reamazePrompt\":\"Let me know if you have any questions!\",\"reamazePromptEnabled\":true,\"reamazeThemeColor\":\"#f5d8d0\",\"reamazePosition\":\"bottom-right\",\"reamazeConfirmationMessage\":\"Thanks! Your message has been submitted. We'll get back to you here or via email.\",\"reamazeAvatarImage\":\"\",\"widgetId\":\"822d5ae4-91d2-4f47-8375-11fe8d781bc4\",\"section\":\"default\",\"category\":\"neutral\",\"locale\":\"en-IN\",\"env\":\"production\",\"renderMode\":\"PUBLISH\"}"),context:JSON.parse("{\"widgetId\":\"822d5ae4-91d2-4f47-8375-11fe8d781bc4\",\"widgetType\":\"MESSAGING\",\"widgetPreset\":\"messaging1\",\"section\":\"default\",\"category\":\"neutral\",\"fontSize\":\"medium\",\"fontFamily\":\"alternate\",\"websiteThemeOverrides\":{},\"widgetThemeOverrides\":{}}"),contextKey:'context-bs-1',radpack:"@widget/MESSAGING/bs-Component"});
document.getElementById('page-22091').addEventListener('click', function() {}, false);
var t=document.createElement("script");t.type="text/javascript",t.addEventListener("load",()=>{window.tti.calculateTTI(({name:t,value:e}={})=>{let i={"wam_site_hasPopupWidget":false,"wam_site_hasMessagingWidget":true,"wam_site_headerTreatment":false,"wam_site_hasSlideshow":false,"wam_site_hasFreemiumBanner":false,"wam_site_homepageFirstWidgetType":"ABOUT","wam_site_homepageFirstWidgetPreset":"about10","wam_site_businessCategory":"personal","wam_site_theme":"layout27","wam_site_locale":"en-IN","wam_site_fontPack":"righteous","wam_site_cookieBannerEnabled":true,"wam_site_membershipEnabled":true,"wam_site_hasHomepageHTML":false,"wam_site_hasHomepageShop":false,"wam_site_hasHomepageOla":false,"wam_site_hasHomepageBlog":false,"wam_site_hasShop":false,"wam_site_hasOla":false,"wam_site_planType":"commerce","wam_site_isHomepage":true,"wam_site_htmlWidget":false};window.networkInfo&&window.networkInfo.downlink&&(i=Object.assign({},i,{["wam_site_networkSpeed"]:window.networkInfo.downlink.toFixed(2)})),window.tti.setCustomProperties(i),window.tti._collectVitals({name:t,value:e})})}),t.setAttribute("src","//img1.wsimg.com/traffic-assets/js/tccl-tti.min.js"),document.body.appendChild(t);