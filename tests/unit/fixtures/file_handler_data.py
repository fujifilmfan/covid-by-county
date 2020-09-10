#!/usr/bin/env python

from pathlib import Path

_PACKAGE_DIR = Path(__file__).absolute().parent  # .../unit
_FIXTURES = Path.joinpath(_PACKAGE_DIR, 'fixtures')  # .../unit/fixtures
_HTML = Path.joinpath(_FIXTURES, 'html')  # .../unit/fixtures/html

four_csv_links = """
    <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
        <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
            <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
        </div>
        <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/03-30-2020.csv" id="a7a98a54fb19ff5133d028b319f3b6d3-9ef832ca79a5a74882e6238f14638c6861e10055" title="03-30-2020.csv">03-30-2020.csv</a></span>
        </div>
        <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/726f73094b9bc5cb786e2c4aa9cdc23cf565ed5c" title="Correction for Hainan, China">Correction for Hainan, China</a></span>
        </div>
        <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
            Apr 13, 2020
        </div>
    </div>
    <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
    
        <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
            <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
        </div>
        <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/03-31-2020.csv" id="0f8ced6072413e0442845ba3e0efaf5d-08490e499f7b30c33d94503ec3102e47a74cdc81" title="03-31-2020.csv">03-31-2020.csv</a></span>
        </div>
        <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/db2036b77e5f1419136c28ae428e3aba8c9b9829" title="Correction for Hainan, China">Correction for Hainan, China</a></span>
        </div>
        <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
            Apr 13, 2020
        </div>
    </div>
    <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
    
        <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
            <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
        </div>
        <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv" id="fc641531f8305bef113a4c9a576cc2c2-eb0e137d2a2bbc905a91787a2e609e55ea2013bf" title="04-01-2020.csv">04-01-2020.csv</a></span>
        </div>
        <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/30ce7eb4b0a6a37b274f12cda350554b95609baa" title="updated data">updated data</a></span>
        </div>
        <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
            Apr 16, 2020
        </div>
    </div>
    <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
    
        <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
            <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
        </div>
        <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/04-02-2020.csv" id="604a487f4afde7559e6c986fbeaf480c-7ca74de984656935d468b597ed5692b2f2ff0adc" title="04-02-2020.csv">04-02-2020.csv</a></span>
        </div>
        <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/53324cb417b5037ee7146a758ebf880ff47d4d56" title="adjust incorrect data">adjust incorrect data</a></span>
        </div>
        <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
            Apr 9, 2020
        </div>
    </div>
"""

page_with_zero_csv_links = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>COVID-19/csse_covid_19_data/csse_covid_19_daily_reports at master CSSEGISandData/COVID-19 GitHub</title>
    </head>
    <body>
        <meta charset="utf-8">
        <link href="https://github.githubassets.com" rel="dns-prefetch">
        <link href="https://avatars0.githubusercontent.com" rel="dns-prefetch">
        <link href="https://avatars1.githubusercontent.com" rel="dns-prefetch">
        <link href="https://avatars2.githubusercontent.com" rel="dns-prefetch">
        <link href="https://avatars3.githubusercontent.com" rel="dns-prefetch">
        <link href="https://github-cloud.s3.amazonaws.com" rel="dns-prefetch">
        <link href="https://user-images.githubusercontent.com/" rel="dns-prefetch">
        <link href="https://github.githubassets.com/assets/frameworks-8c550109d58e0353afdf1a37a05301c2.css" media="all" rel="stylesheet">
        <link href="https://github.githubassets.com/assets/site-6740e47db15be170e8725a8f816d30e1.css" media="all" rel="stylesheet">
        <link href="https://github.githubassets.com/assets/github-503b06468b70c7693a91b7c35fd8c77c.css" media="all" rel="stylesheet">
        <meta content="width=device-width" name="viewport">
        <meta content="Novel Coronavirus (COVID-19) Cases, provided by JHU CSSE - CSSEGISandData/COVID-19" name="description">
        <link href="/opensearch.xml" rel="search" title="GitHub" type="application/opensearchdescription+xml">
        <link href="https://github.com/fluidicon.png" rel="fluid-icon" title="GitHub">
        <meta content="1401488693436528" property="fb:app_id">
        <meta content="app-id=1477376905" name="apple-itunes-app">
        <meta content="https://avatars2.githubusercontent.com/u/60674295?s=400&amp;v=4" name="twitter:image:src">
        <meta content="@github" name="twitter:site">
        <meta content="summary" name="twitter:card">
        <meta content="CSSEGISandData/COVID-19" name="twitter:title">
        <meta content="Novel Coronavirus (COVID-19) Cases, provided by JHU CSSE - CSSEGISandData/COVID-19" name="twitter:description">
        <meta content="https://avatars2.githubusercontent.com/u/60674295?s=400&amp;v=4" property="og:image">
        <meta content="GitHub" property="og:site_name">
        <meta content="object" property="og:type">
        <meta content="CSSEGISandData/COVID-19" property="og:title">
        <meta content="https://github.com/CSSEGISandData/COVID-19" property="og:url">
        <meta content="Novel Coronavirus (COVID-19) Cases, provided by JHU CSSE - CSSEGISandData/COVID-19" property="og:description">
        <link href="https://github.githubassets.com/" rel="assets">
        <meta content="C876:3CCD:1A102E3:2A1A4EB:5F573724" data-pjax-transient="true" name="request-id">
        <meta content="c2feac881df0c0cf0c0bc22fb7e76eda7d387543" data-pjax-transient="true" name="html-safe-nonce">
        <meta content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJDODc2OjNDQ0Q6MUExMDJFMzoyQTFBNEVCOjVGNTczNzI0IiwidmlzaXRvcl9pZCI6IjM0MzAyMDYzODAyMjA4MjMzMzIiLCJyZWdpb25fZWRnZSI6ImlhZCIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-pjax-transient="true" name="visitor-payload">
        <meta content="37a7b16ce572f6390642a42b6b2f2b85acc3c200c4c601bd9fa9bb88ab1aed70" data-pjax-transient="true" name="visitor-hmac">
        <meta content="false" data-pjax-transient="true" name="cookie-consent-required">
        <meta content="repository:238316428" data-pjax-transient="" name="hovercard-subject-tag">
        <meta content="repository,source-code" data-pjax-transient="true" name="github-keyboard-shortcuts">
        <meta data-pjax-transient="" name="selected-link">
        <meta content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY" name="google-site-verification">
        <meta content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU" name="google-site-verification">
        <meta content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA" name="google-site-verification">
        <meta content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc" name="google-site-verification">
        <meta content="collector.githubapp.com" name="octolytics-host">
        <meta content="github" name="octolytics-app-id">
        <meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url">
        <meta class="js-octo-ga-id" content="" name="octolytics-dimension-ga_id">
        <meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate" data-pjax-transient="true" name="analytics-location">
        <meta content="UA-3769691-2" name="google-analytics">
        <meta class="js-ga-set" content="Responsive" data-pjax-transient="" name="dimension10">
        <meta class="js-ga-set" content="Logged Out" name="dimension1">
        <meta content="github.com" name="hostname">
        <meta content="" name="user-login">
        <meta content="github.com" name="expected-hostname">
        <meta content="MARKETPLACE_PENDING_INSTALLATIONS" name="enabled-features">
        <meta content="5952e37321a36a20ef488a3f02341e00" http-equiv="x-pjax-version">
        <link href="https://github.com/CSSEGISandData/COVID-19/commits/master.atom" rel="alternate" title="Recent Commits to COVID-19:master" type="application/atom+xml">
        <meta content="github.com/CSSEGISandData/COVID-19 git https://github.com/CSSEGISandData/COVID-19.git" name="go-import">
        <meta content="60674295" name="octolytics-dimension-user_id">
        <meta content="CSSEGISandData" name="octolytics-dimension-user_login">
        <meta content="238316428" name="octolytics-dimension-repository_id">
        <meta content="CSSEGISandData/COVID-19" name="octolytics-dimension-repository_nwo">
        <meta content="true" name="octolytics-dimension-repository_public">
        <meta content="false" name="octolytics-dimension-repository_is_fork">
        <meta content="238316428" name="octolytics-dimension-repository_network_root_id">
        <meta content="CSSEGISandData/COVID-19" name="octolytics-dimension-repository_network_root_nwo">
        <meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown">
        <link data-pjax-transient="" href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports" rel="canonical">
        <meta content="https://api.github.com/_private/browser/stats" name="browser-stats-url">
        <meta content="https://api.github.com/_private/browser/errors" name="browser-errors-url">
        <link href="https://github.githubassets.com/pinned-octocat.svg" rel="mask-icon">
        <link class="js-site-favicon" href="https://github.githubassets.com/favicons/favicon.png" rel="alternate icon" type="image/png">
        <link class="js-site-favicon" href="https://github.githubassets.com/favicons/favicon.svg" rel="icon" type="image/svg+xml">
        <meta content="#1e2327" name="theme-color">
        <link href="/manifest.json" rel="manifest">
        <div class="position-relative js-header-wrapper">
            <a class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content" href="#start-of-content">Skip to content</a><span class="progress-pjax-loader width-full js-pjax-loader-bar Progress position-fixed"><span class="Progress-item progress-pjax-loader-bar" style="background-color: #79b8ff;width: 0%;"></span></span>
            <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
    
                <div class="container-xl d-lg-flex flex-items-center p-responsive">
    
                    <div class="d-flex flex-justify-between flex-items-center">
                        <a aria-label="Homepage" class="mr-4" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark" href="https://github.com/"><svg aria-hidden="true" class="octicon octicon-mark-github text-white" height="32" version="1.1" viewbox="0 0 16 16" width="32">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg></a>
                        <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
    
                        </div>
                        <div class="d-flex flex-items-center">
                            <a class="d-inline-block d-lg-none f5 text-white no-underline border border-gray-dark rounded-2 px-2 py-1 mr-3 mr-sm-5" data-ga-click="Sign up, click to sign up for account, ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate;ref_cta:Sign up;ref_loc:header logged out" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="8daadfbd9805d840f27a699224b4231c81310f9721e1337ccc1a5e133854e71f" href="/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&amp;source=header-repo">Sign&nbsp;up</a>  <button aria-expanded="false" aria-label="Toggle navigation" class="btn-link d-lg-none mt-1 js-details-target" type="button"><svg aria-hidden="true" class="octicon octicon-three-bars text-white" height="24" version="1.1" viewbox="0 0 16 16" width="24">
                            <path d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z" fill-rule="evenodd"></path></svg></button>
                        </div>
                    </div>
                    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
    
                        <div class="d-flex d-lg-none flex-justify-end border-bottom bg-gray-light p-3">
                            <button aria-expanded="false" aria-label="Toggle navigation" class="btn-link js-details-target" type="button"><svg aria-hidden="true" class="octicon octicon-x text-gray" height="24" version="1.1" viewbox="0 0 24 24" width="24">
                            <path d="M5.72 5.72a.75.75 0 011.06 0L12 10.94l5.22-5.22a.75.75 0 111.06 1.06L13.06 12l5.22 5.22a.75.75 0 11-1.06 1.06L12 13.06l-5.22 5.22a.75.75 0 01-1.06-1.06L10.94 12 5.72 6.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button>
                        </div>
                        <nav aria-label="Global" class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0">
    
                            <ul class="d-lg-flex list-style-none">
                                <li style="list-style: none"></li>
                                <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
                                    <details class="HeaderMenu-details details-overlay details-reset width-full">
    
                                        <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                                            Why GitHub?<svg class="icon-chevon-down-mktg position-absolute position-lg-relative" viewbox="0 0 14 8" x="0px" y="0px">
                                            <path d="M1,1l6.2,6L13,1"></path></svg>
                                        </summary>
                                        <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                                            <a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features" href="/features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                            <ul class="list-style-none f5 pb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review" href="/features/code-review/">Code review</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management" href="/features/project-management/">Project management</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations" href="/features/integrations">Integrations</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions" href="/features/actions">Actions</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Packages" href="/features/packages">Packages</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Security" href="/features/security">Security</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management" href="/features#team-management">Team management</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting" href="/features#hosting">Hosting</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix hide-xl">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Mobile" href="/mobile">Mobile</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories" href="/customer-stories">Customer stories <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security" href="/security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </details>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3"><a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Team" href="/team">Team</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3"><a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise" href="/enterprise">Enterprise</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
                                    <details class="HeaderMenu-details details-overlay details-reset width-full">
    
                                        <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                                            Explore<svg class="icon-chevon-down-mktg position-absolute position-lg-relative" viewbox="0 0 14 8" x="0px" y="0px">
                                            <path d="M1,1l6.2,6L13,1"></path></svg>
                                        </summary>
                                        <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
    
                                            <ul class="list-style-none mb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore" href="/explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn &amp; contribute</h4>
                                            <ul class="list-style-none mb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics" href="/topics">Topics</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections" href="/collections">Collections</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending" href="/trending">Trending</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab" href="https://lab.github.com/">Learning Lab</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides" href="https://opensource.guide">Open source guides</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
                                            <ul class="list-style-none mb-0">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events" href="https://github.com/events">Events</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum" href="https://github.community">Community forum</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education" href="https://education.github.com">GitHub Education</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Stars Program" href="https://stars.github.com">GitHub Stars program</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </details>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3"><a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace" href="/marketplace">Marketplace</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
                                    <details class="HeaderMenu-details details-overlay details-reset width-full">
    
                                        <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                                            Pricing<svg class="icon-chevon-down-mktg position-absolute position-lg-relative" viewbox="0 0 14 8" x="0px" y="0px">
                                            <path d="M1,1l6.2,6L13,1"></path></svg>
                                        </summary>
                                        <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                                            <a class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing" href="/pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                            <ul class="list-style-none mb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare plans" href="/pricing#feature-comparison">Compare plans</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Contact Sales" href="https://enterprise.github.com/contact">Contact Sales</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits" href="/nonprofit">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Education" href="https://education.github.com">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </details>
                                </li>
                                <li style="list-style: none"></li>
                            </ul>
                        </nav>
                        <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
    
                            <div class="d-lg-flex mb-3 mb-lg-0">
    
                                <div aria-expanded="false" aria-haspopup="listbox" aria-label="Search or jump to" aria-owns="jump-to-results" class="header-search header-search-current js-header-search-current flex-auto flex-self-stretch flex-md-self-auto mr-0 mr-md-3 mb-3 mb-md-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to js-header-search-current-jump-to" role="combobox">
    
                                    <div class="position-relative">
                                        <!-- \'"` --><!-- </textarea></xmp> -->
                                        <form accept-charset="UTF-8" action="/CSSEGISandData/COVID-19/search" aria-label="Site" class="js-site-search-form" data-scope-id="238316428" data-scope-type="Repository" data-scoped-search-url="/CSSEGISandData/COVID-19/search" data-unscoped-search-url="/search" method="get" role="search">
                                            <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><input aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search" autocomplete="off" class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable" data-hotkey="s,/" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-scoped-placeholder="Search" data-unscoped-placeholder="Search GitHub" name="q" placeholder="Search" spellcheck="false" type="text" value=""><input class="js-data-jump-to-suggestions-path-csrf" data-csrf="true" type="hidden" value="Fmc6YwmtPQyMav/TxxK81UyJIneQ1Lnu6afZch2ogrRBNSlrEDbtvqQdmkHtf2p8Gmq0riUYhRhgG9pU8QAfcA=="><input class="js-site-search-type-field" name="type" type="hidden"><img alt="" class="mr-2 header-search-key-slash" src="https://github.githubassets.com/images/search-key-slash.svg"></label>
                                            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
                                                <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                <ul class="d-none js-jump-to-suggestions-template-container">
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
                                                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg></label>
                                                    </div> <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28">
                                                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                    </div>
                                                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">In this repository</span> <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">All GitHub</span> <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div>
                                                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">Jump to<span class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div></a> </label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                </ul><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                <ul class="d-none js-jump-to-no-results-template-container">
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span class="text-gray">No suggested jump to results</span></label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                </ul><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                <ul class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container" id="jump-to-results" role="listbox">
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
                                                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg></label>
                                                    </div> <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28">
                                                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                    </div>
                                                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">In this repository</span> <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">All GitHub</span> <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div>
                                                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">Jump to<span class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div></a> </label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
                                                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg></label>
                                                    </div> <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28">
                                                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                    </div>
                                                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">In this repository</span> <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">All GitHub</span> <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div>
                                                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">Jump to<span class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div></a> </label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                </ul><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                            </div><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                        </form>
                                    </div>
                                </div>
                            </div> <a class="HeaderMenu-link no-underline mr-3" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="453f406786f8ed65267f5f57d2c31b709c558aa9409ca1a988f71d251a3ee64b" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19%2Ftree%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_daily_reports">Sign&nbsp;in</a> <a class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1" data-ga-click="Sign up, click to sign up for account, ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate;ref_cta:Sign up;ref_loc:header logged out" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="453f406786f8ed65267f5f57d2c31b709c558aa9409ca1a988f71d251a3ee64b" href="/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&amp;source=header-repo&amp;source_repo=CSSEGISandData%2FCOVID-19">Sign&nbsp;up</a>
                        </div>
                    </div>
                </div>
            </header>
        </div>
        <div class="show-on-focus" id="start-of-content"></div>
        <div id="js-flash-container">
    
            <template class="js-flash-template">
    
                <div class="flash flash-full {{ className }}">
    
                    <div class=" px-2">
                        <button aria-label="Dismiss this message" class="flash-close js-flash-close" type="button"><svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                        <path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button>
                        <div>
                            {{ message }}
                        </div>
                    </div>
                </div>
            </template>
        </div>
        <div class="application-main">
    
            <div class="" itemscope itemtype="http://schema.org/SoftwareSourceCode">
    
                <main data-pjax-container="" id="js-repo-pjax-container">
                    <div class="bg-gray-light pt-3 hide-full-screen mb-5">
    
                        <div class="d-flex mb-3 px-3 px-md-4 px-lg-5">
    
                            <div class="flex-auto min-width-0 width-fit mr-3">
    
                                <h1 class=" d-flex flex-wrap flex-items-center break-word f3 text-normal"><svg aria-hidden="true" class="octicon octicon-repo text-gray" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><span class="author ml-2 flex-self-stretch" itemprop="author"><a class="url fn" data-hovercard-type="user" data-hovercard-url="/users/CSSEGISandData/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/CSSEGISandData" rel="author">CSSEGISandData</a></span> <span class="mx-1 flex-self-stretch">/</span><strong class="mr-2 flex-self-stretch" itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/CSSEGISandData/COVID-19">COVID-19</a></strong> </h1>
                            </div>
                            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
                                <li style="list-style: none"></li>
                                <li><a aria-label="You must be signed in to watch a repository" class="tooltipped tooltipped-s btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="8bcf781b787d7a363448427b5e6be6e4bba67f0bb4d18bbe9540c2662563d229" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19" rel="nofollow"><svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z" fill-rule="evenodd"></path></svg>Watch</a> <a aria-label="911 users are watching this repository" class="social-count" href="/CSSEGISandData/COVID-19/watchers">911</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li><a aria-label="You must be signed in to star a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:238316428,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ef2e47d75f6298a99bda8c34181197c7e0663581b1beefbf78bbd5d351aef126" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19" rel="nofollow"><svg aria-hidden="true" class="octicon octicon-star v-align-text-bottom" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" fill-rule="evenodd"></path></svg>Star</a><a aria-label="23842 users starred this repository" class="social-count js-social-count" href="/CSSEGISandData/COVID-19/stargazers">23.8k</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li><a aria-label="You must be signed in to fork a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:238316428,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="b27e52197fadff8c461ad531c53f1a66acc46a4ec178ce946976f83749e056e4" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19" rel="nofollow"><svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z" fill-rule="evenodd"></path></svg>Fork</a><a aria-label="14983 users forked this repository" class="social-count" href="/CSSEGISandData/COVID-19/network/members">15k</a>
                                </li>
                                <li style="list-style: none"></li>
                            </ul>
                        </div>
                        <nav aria-label="Repository" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5 bg-gray-light" data-pjax="#js-repo-pjax-container">
    
                            <ul class="UnderlineNav-body list-style-none">
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item selected UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Code tab" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /CSSEGISandData/COVID-19" data-tab-item="code-tab" href="/CSSEGISandData/COVID-19"><svg aria-hidden="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z" fill-rule="evenodd"></path></svg><span data-content="Code">Code</span><span class="Counter" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Issues tab" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /CSSEGISandData/COVID-19/issues" data-tab-item="issues-tab" href="/CSSEGISandData/COVID-19/issues"><svg aria-hidden="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" fill-rule="evenodd"></path></svg><span data-content="Issues">Issues</span><span class="Counter" title="1,307">1.3k</span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Pull requests tab" data-hotkey="g p" data-selected-links="repo_pulls checks /CSSEGISandData/COVID-19/pulls" data-tab-item="pull-requests-tab" href="/CSSEGISandData/COVID-19/pulls"><svg aria-hidden="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z" fill-rule="evenodd"></path></svg><span data-content="Pull requests">Pull requests</span><span class="Counter" title="273">273</span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Actions tab" data-hotkey="g a" data-selected-links="repo_actions /CSSEGISandData/COVID-19/actions" data-tab-item="actions-tab" href="/CSSEGISandData/COVID-19/actions"><svg aria-hidden="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z" fill-rule="evenodd"></path></svg><span data-content="Actions">Actions</span><span class="Counter" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Projects tab" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /CSSEGISandData/COVID-19/projects" data-tab-item="projects-tab" href="/CSSEGISandData/COVID-19/projects"><svg aria-hidden="true" class="octicon octicon-project UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><span data-content="Projects">Projects</span><span class="Counter" hidden="hidden" title="0">0</span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Security tab" data-hotkey="g s" data-selected-links="security overview alerts policy token_scanning code_scanning /CSSEGISandData/COVID-19/security" data-tab-item="security-tab" href="/CSSEGISandData/COVID-19/security"><svg aria-hidden="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z" fill-rule="evenodd"></path></svg><span data-content="Security">Security</span><span class="js-security-tab-count Counter" data-url="/CSSEGISandData/COVID-19/security/overall-count" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Insights tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people /CSSEGISandData/COVID-19/pulse" data-tab-item="insights-tab" href="/CSSEGISandData/COVID-19/pulse"><svg aria-hidden="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z" fill-rule="evenodd"></path></svg><span data-content="Insights">Insights</span><span class="Counter" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                            </ul>
                            <div class="position-absolute right-0 pr-3 pr-md-4 pr-lg-5 js-responsive-underlinenav-overflow" style="visibility:hidden;">
    
                                <details class="details-overlay details-reset position-relative">
    
                                    <summary role="button">
    
                                    </summary>
                                    <div class="UnderlineNav-item mr-0 border-0">
                                        <svg aria-hidden="true" class="octicon octicon-kebab-horizontal" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                        <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg><span class="sr-only">More</span>
                                    </div>
                                    <ul>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="code-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19" href="/CSSEGISandData/COVID-19" role="menuitem">Code</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="issues-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/issues" href="/CSSEGISandData/COVID-19/issues" role="menuitem">Issues</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="pull-requests-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/pulls" href="/CSSEGISandData/COVID-19/pulls" role="menuitem">Pull requests</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="actions-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/actions" href="/CSSEGISandData/COVID-19/actions" role="menuitem">Actions</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="projects-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/projects" href="/CSSEGISandData/COVID-19/projects" role="menuitem">Projects</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="security-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/security" href="/CSSEGISandData/COVID-19/security" role="menuitem">Security</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="insights-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/pulse" href="/CSSEGISandData/COVID-19/pulse" role="menuitem">Insights</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                    </ul>
                                </details>
                            </div>
                        </nav>
                    </div>
                    <div class="container-xl clearfix new-discussion-timeline px-3 px-md-4 px-lg-5">
    
                        <div class="repository-content">
    
                            <div class="file-navigation mb-3 d-flex flex-items-start">
    
                                <div class="position-relative">
    
                                    <details class="details-reset details-overlay mr-0 mb-0" id="branch-select-menu">
    
                                        <summary class="btn css-truncate" data-hotkey="w" title="Switch branches or tags">
                                            <svg aria-hidden="true" class="octicon octicon-git-branch text-gray" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                            <path d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z" fill-rule="evenodd"></path></svg><span class="css-truncate-target" data-menu-button="">master</span><span class="dropdown-caret"></span>
                                        </summary>
                                        <div class="SelectMenu-modal">
                                             <svg aria-hidden="true" class="octicon octicon-octoface anim-pulse" height="32" version="1.1" viewbox="0 0 24 24" width="32">
                                            <path d="M7.75 11c-.69 0-1.25.56-1.25 1.25v1.5a1.25 1.25 0 102.5 0v-1.5C9 11.56 8.44 11 7.75 11zm1.27 4.5a.469.469 0 01.48-.5h5a.47.47 0 01.48.5c-.116 1.316-.759 2.5-2.98 2.5s-2.864-1.184-2.98-2.5zm7.23-4.5c-.69 0-1.25.56-1.25 1.25v1.5a1.25 1.25 0 102.5 0v-1.5c0-.69-.56-1.25-1.25-1.25z"></path>
                                            <path d="M21.255 3.82a1.725 1.725 0 00-2.141-1.195c-.557.16-1.406.44-2.264.866-.78.386-1.647.93-2.293 1.677A18.442 18.442 0 0012 5c-.93 0-1.784.059-2.569.17-.645-.74-1.505-1.28-2.28-1.664a13.876 13.876 0 00-2.265-.866 1.725 1.725 0 00-2.141 1.196 23.645 23.645 0 00-.69 3.292c-.125.97-.191 2.07-.066 3.112C1.254 11.882 1 13.734 1 15.527 1 19.915 3.13 23 12 23c8.87 0 11-3.053 11-7.473 0-1.794-.255-3.647-.99-5.29.127-1.046.06-2.15-.066-3.125a23.652 23.652 0 00-.689-3.292zM20.5 14c.5 3.5-1.5 6.5-8.5 6.5s-9-3-8.5-6.5c.583-4 3-6 8.5-6s7.928 2 8.5 6z" fill-rule="evenodd"></path></svg>
                                        </div>
                                    </details>
                                </div>
                                <div class="flex-1 mx-2 flex-self-center f4">
    
                                    <div class="d-none d-sm-block">
                                        <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19"><span>COVID-19</span></a></span></span><span class="mx-1">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data"><span>csse_covid_19_data</span></a></span><span class="mx-1">/</span><strong class="final-path">csse_covid_19_daily_reports</strong><span class="mx-1">/</span>
                                    </div>
                                </div>
                                <div class="d-flex">
                                    <a class="btn mr-2 d-none d-md-block" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FIND_FILE_BUTTON&quot;,&quot;repository_id&quot;:238316428,&quot;originating_url&quot;:&quot;https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="f69eeff120eac2d87ab515142f9599079e40e011adadb6a8a0e21f336af95f93" data-pjax="true" href="/CSSEGISandData/COVID-19/find/master">Go to file</a>
                                </div>
                            </div>
                            <div class="f4 mt-3 mb-3 d-sm-none">
                                <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19"><span>COVID-19</span></a></span></span><span class="mx-1">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data"><span>csse_covid_19_data</span></a></span><span class="mx-1">/</span><strong class="final-path">csse_covid_19_daily_reports</strong><span class="separator mx-1">/</span>
                            </div>
                            <div class="Box mb-3">
    
                                <div class="Box-header Box-header--blue position-relative">
    
                                    <h2 class="sr-only">Latest commit</h2>
                                    <div class="js-details-container Details d-flex rounded-top-1 flex-items-center flex-wrap" data-issue-and-pr-hovercards-enabled="">
    
                                        <div class="flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1 hx_avatar_stack_commit">
    
                                            <div class="AvatarStack flex-self-start">
    
                                                <div aria-label="CSSEGISandData" class="AvatarStack-body">
                                                    <a class="avatar avatar-user" data-hovercard-type="user" data-hovercard-url="/users/CSSEGISandData/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" data-skip-pjax="true" href="/CSSEGISandData" style="width:24px;height:24px;"><img alt="@CSSEGISandData" class=" avatar-user" height="24" src="https://avatars1.githubusercontent.com/u/60674295?s=60&amp;u=cda3e09cda856b17dbc71dbd50b87f75955e7e48&amp;v=4" width="24"></a>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="flex-1 d-flex flex-items-center ml-3 min-width-0">
    
                                            <div class="css-truncate css-truncate-overflow text-gray">
                                                 <a class="commit-author user-mention" href="/CSSEGISandData/COVID-19/commits?author=CSSEGISandData" title="View all commits by CSSEGISandData">CSSEGISandData</a> <span class="d-none d-sm-inline"><a class="link-gray-dark" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6" title="Automated update">Automated update</a></span>
                                            </div><span class="hidden-text-expander ml-2 d-inline-block d-inline-block d-lg-none"><button aria-expanded="false" class="hx_bg-black-fade-15 text-gray-dark ellipsis-expander js-details-target" type="button"><span class="hidden-text-expander ml-2 d-inline-block d-inline-block d-lg-none">&hellip;</span></button></span>
                                            <div class="d-flex flex-auto flex-justify-end ml-3 flex-items-baseline">
                                                 <a class="f6 link-gray text-mono ml-2 d-none d-lg-inline" data-pjax="" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6">0bf4d22</a><a class="link-gray ml-2" data-pjax="" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6">Sep 8, 2020</a>
                                            </div>
                                        </div>
                                        <div class="pl-0 pl-md-5 flex-order-1 width-full Details-content--hidden">
    
                                            <div class="mt-2">
                                                <a class="link-gray-dark text-bold" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6">Automated update</a>
                                            </div>
                                            <div class="d-flex flex-items-center">
                                                <span class="text-gray-dark text-mono d-lg-none hx_bg-black-fade-15 px-1 rounded-1 text-small mt-2">0bf4d22</span>
                                            </div>
                                        </div>
                                        <div class="flex-shrink-0">
    
                                            <h2 class="sr-only">Git stats</h2>
                                            <ul class="list-style-none d-flex">
                                                <li style="list-style: none"></li>
                                                <li class="ml-0 ml-md-3"><a class="pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 link-gray-dark no-underline no-wrap" data-pjax="" href="/CSSEGISandData/COVID-19/commits/master/csse_covid_19_data/csse_covid_19_daily_reports"><svg aria-hidden="true" class="octicon octicon-history text-gray" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                                    <path d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z" fill-rule="evenodd"></path></svg><span class="d-none d-sm-inline"><strong>History</strong></span> </a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                                <h2 class="sr-only" id="files">Files</h2><a class="d-none js-permalink-shortcut" data-hotkey="y" href="/CSSEGISandData/COVID-19/tree/0bf4d22e5205622c14962f27d596c067086a4dc6/csse_covid_19_data/csse_covid_19_daily_reports">Permalink</a>
                                <div class="flash flash-full flash-error include-fragment-error py-2">
                                    <svg aria-hidden="true" class="octicon octicon-alert mr-2" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg> Failed to load latest commit information.
                                </div>
                                <div class="js-details-container Details">
    
                                    <div aria-labelledby="files" class="Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-block" data-pjax="" role="grid">
    
                                        <div class="sr-only" role="row">
    
                                            <div role="columnheader">
                                                Type
                                            </div>
                                            <div role="columnheader">
                                                Name
                                            </div>
                                            <div class="d-none d-md-block" role="columnheader">
                                                Latest commit message
                                            </div>
                                            <div role="columnheader">
                                                Commit time
                                            </div>
                                        </div>
                                        <div class="Box-row Box-row--focus-gray p-0 d-flex js-navigation-item" role="row">
    
                                            <div class="flex-auto min-width-0 col-md-2" role="rowheader">
                                                <a class="js-navigation-open d-block py-2 px-3" href="/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data" rel="nofollow" title="Go to parent directory"><span class="text-bold text-center d-inline-block" style="min-width: 16px;">. .</span></a>
                                            </div>
                                            <div class="d-none d-md-block" role="gridcell"></div>
                                            <div role="gridcell"></div>
                                        </div>
                                        <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
    
                                            <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
                                                <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
                                                <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
                                            </div>
                                            <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/.gitignore" id="a084b794bc0759e7a6b77810e01874f2-496ee2ca6a2f08396a4076fe43dedf3dc0da8b6d" title=".gitignore">.gitignore</a></span>
                                            </div>
                                            <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/ddd8cf43bd6a3c40d12f48668f5ea39e7c42f708" title="update">update</a></span>
                                            </div>
                                            <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
                                                Feb 14, 2020
                                            </div>
                                        </div>
                                        <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
    
                                            <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
                                                <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
                                                <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
                                            </div>
                                            <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/README.md" id="04c6e90faac2675aa89e2176d2eec7d8-e69de29bb2d1d6434b8b29ae775ad8c2e48c5391" title="README.md">README.md</a></span>
                                            </div>
                                            <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/7e3dbcde3f44c7a312d3bd010cbe36fa609dd869" title="update">update</a></span>
                                            </div>
                                            <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
                                                Feb 14, 2020
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
        <div class="footer container-xl width-full p-responsive" role="contentinfo">
    
            <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light">
    
                <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to status, text:status" href="https://githubstatus.com/">Status</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li>
                        <a data-ga-click="Footer, go to help, text:help" href="https://docs.github.com">Help</a>
                    </li>
                    <li style="list-style: none"></li>
                </ul> <a aria-label="Homepage" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com" title="GitHub"><svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewbox="0 0 16 16" width="24">
                <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg></a>
                <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to Pricing, text:Pricing" href="https://github.com/pricing">Pricing</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to api, text:api" href="https://docs.github.com">API</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to training, text:training" href="https://services.github.com">Training</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to blog, text:blog" href="https://github.blog">Blog</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li>
                        <a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a>
                    </li>
                    <li style="list-style: none"></li>
                </ul>
            </div>
            <div class="d-flex flex-justify-center pb-6">
                <span class="f6 text-gray-light"></span>
            </div>
        </div>
        <div class="ajax-error-message flash flash-error" id="ajax-error-message">
            <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg><button aria-label="Dismiss error" class="flash-close js-ajax-error-dismiss" type="button"><svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button> You can perform that action at this time.
        </div>
        <script async="async" data-src="https://github.githubassets.com/assets/compat-bootstrap-6e7ff7ac.js" id="js-conditional-compat" type="application/javascript">
        </script>
        <script src="https://github.githubassets.com/assets/environment-bootstrap-0b18da31.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/vendor-d2216e0f.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/frameworks-708fa234.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/behaviors-bootstrap-08dae8c4.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/contributions-spider-graph-36a4ea81.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./drag-drop.js" data-src="https://github.githubassets.com/assets/drag-drop-ad7fde7d.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./image-crop-element-loader.js" data-src="https://github.githubassets.com/assets/image-crop-element-loader-88bb82db.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./jump-to.js" data-src="https://github.githubassets.com/assets/jump-to-402b99bd.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./profile-pins-element.js" data-src="https://github.githubassets.com/assets/profile-pins-element-1f359478.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./randomColor.js" data-src="https://github.githubassets.com/assets/randomColor-a840affe.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./sortable-behavior.js" data-src="https://github.githubassets.com/assets/sortable-behavior-bcaeeb46.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./tweetsodium.js" data-src="https://github.githubassets.com/assets/tweetsodium-987aac13.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./user-status-submit.js" data-src="https://github.githubassets.com/assets/user-status-submit-eb836b74.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/repositories-dd933f65.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/github-bootstrap-83b909b4.js" type="application/javascript">
        </script>
        <div class="js-stale-session-flash flash flash-warn flash-banner">
            <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg><span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span><span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
        </div>
        <template id="site-details-dialog">
    
            <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open="">
    
                <summary aria-label="Close dialog" role="button"></summary> <button aria-label="Close dialog" class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" data-close-dialog="" type="button"><svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                <path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button>
                <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
            </details>
        </template>
        <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
    
            <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
    
            </div>
        </div>
    </body>
    </html>
"""

page_with_four_csv_links = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>COVID-19/csse_covid_19_data/csse_covid_19_daily_reports at master CSSEGISandData/COVID-19 GitHub</title>
    </head>
    <body>
        <meta charset="utf-8">
        <link href="https://github.githubassets.com" rel="dns-prefetch">
        <link href="https://avatars0.githubusercontent.com" rel="dns-prefetch">
        <link href="https://avatars1.githubusercontent.com" rel="dns-prefetch">
        <link href="https://avatars2.githubusercontent.com" rel="dns-prefetch">
        <link href="https://avatars3.githubusercontent.com" rel="dns-prefetch">
        <link href="https://github-cloud.s3.amazonaws.com" rel="dns-prefetch">
        <link href="https://user-images.githubusercontent.com/" rel="dns-prefetch">
        <link href="https://github.githubassets.com/assets/frameworks-8c550109d58e0353afdf1a37a05301c2.css" media="all" rel="stylesheet">
        <link href="https://github.githubassets.com/assets/site-6740e47db15be170e8725a8f816d30e1.css" media="all" rel="stylesheet">
        <link href="https://github.githubassets.com/assets/github-503b06468b70c7693a91b7c35fd8c77c.css" media="all" rel="stylesheet">
        <meta content="width=device-width" name="viewport">
        <meta content="Novel Coronavirus (COVID-19) Cases, provided by JHU CSSE - CSSEGISandData/COVID-19" name="description">
        <link href="/opensearch.xml" rel="search" title="GitHub" type="application/opensearchdescription+xml">
        <link href="https://github.com/fluidicon.png" rel="fluid-icon" title="GitHub">
        <meta content="1401488693436528" property="fb:app_id">
        <meta content="app-id=1477376905" name="apple-itunes-app">
        <meta content="https://avatars2.githubusercontent.com/u/60674295?s=400&amp;v=4" name="twitter:image:src">
        <meta content="@github" name="twitter:site">
        <meta content="summary" name="twitter:card">
        <meta content="CSSEGISandData/COVID-19" name="twitter:title">
        <meta content="Novel Coronavirus (COVID-19) Cases, provided by JHU CSSE - CSSEGISandData/COVID-19" name="twitter:description">
        <meta content="https://avatars2.githubusercontent.com/u/60674295?s=400&amp;v=4" property="og:image">
        <meta content="GitHub" property="og:site_name">
        <meta content="object" property="og:type">
        <meta content="CSSEGISandData/COVID-19" property="og:title">
        <meta content="https://github.com/CSSEGISandData/COVID-19" property="og:url">
        <meta content="Novel Coronavirus (COVID-19) Cases, provided by JHU CSSE - CSSEGISandData/COVID-19" property="og:description">
        <link href="https://github.githubassets.com/" rel="assets">
        <meta content="C876:3CCD:1A102E3:2A1A4EB:5F573724" data-pjax-transient="true" name="request-id">
        <meta content="c2feac881df0c0cf0c0bc22fb7e76eda7d387543" data-pjax-transient="true" name="html-safe-nonce">
        <meta content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJDODc2OjNDQ0Q6MUExMDJFMzoyQTFBNEVCOjVGNTczNzI0IiwidmlzaXRvcl9pZCI6IjM0MzAyMDYzODAyMjA4MjMzMzIiLCJyZWdpb25fZWRnZSI6ImlhZCIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-pjax-transient="true" name="visitor-payload">
        <meta content="37a7b16ce572f6390642a42b6b2f2b85acc3c200c4c601bd9fa9bb88ab1aed70" data-pjax-transient="true" name="visitor-hmac">
        <meta content="false" data-pjax-transient="true" name="cookie-consent-required">
        <meta content="repository:238316428" data-pjax-transient="" name="hovercard-subject-tag">
        <meta content="repository,source-code" data-pjax-transient="true" name="github-keyboard-shortcuts">
        <meta data-pjax-transient="" name="selected-link">
        <meta content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY" name="google-site-verification">
        <meta content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU" name="google-site-verification">
        <meta content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA" name="google-site-verification">
        <meta content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc" name="google-site-verification">
        <meta content="collector.githubapp.com" name="octolytics-host">
        <meta content="github" name="octolytics-app-id">
        <meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url">
        <meta class="js-octo-ga-id" content="" name="octolytics-dimension-ga_id">
        <meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate" data-pjax-transient="true" name="analytics-location">
        <meta content="UA-3769691-2" name="google-analytics">
        <meta class="js-ga-set" content="Responsive" data-pjax-transient="" name="dimension10">
        <meta class="js-ga-set" content="Logged Out" name="dimension1">
        <meta content="github.com" name="hostname">
        <meta content="" name="user-login">
        <meta content="github.com" name="expected-hostname">
        <meta content="MARKETPLACE_PENDING_INSTALLATIONS" name="enabled-features">
        <meta content="5952e37321a36a20ef488a3f02341e00" http-equiv="x-pjax-version">
        <link href="https://github.com/CSSEGISandData/COVID-19/commits/master.atom" rel="alternate" title="Recent Commits to COVID-19:master" type="application/atom+xml">
        <meta content="github.com/CSSEGISandData/COVID-19 git https://github.com/CSSEGISandData/COVID-19.git" name="go-import">
        <meta content="60674295" name="octolytics-dimension-user_id">
        <meta content="CSSEGISandData" name="octolytics-dimension-user_login">
        <meta content="238316428" name="octolytics-dimension-repository_id">
        <meta content="CSSEGISandData/COVID-19" name="octolytics-dimension-repository_nwo">
        <meta content="true" name="octolytics-dimension-repository_public">
        <meta content="false" name="octolytics-dimension-repository_is_fork">
        <meta content="238316428" name="octolytics-dimension-repository_network_root_id">
        <meta content="CSSEGISandData/COVID-19" name="octolytics-dimension-repository_network_root_nwo">
        <meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown">
        <link data-pjax-transient="" href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports" rel="canonical">
        <meta content="https://api.github.com/_private/browser/stats" name="browser-stats-url">
        <meta content="https://api.github.com/_private/browser/errors" name="browser-errors-url">
        <link href="https://github.githubassets.com/pinned-octocat.svg" rel="mask-icon">
        <link class="js-site-favicon" href="https://github.githubassets.com/favicons/favicon.png" rel="alternate icon" type="image/png">
        <link class="js-site-favicon" href="https://github.githubassets.com/favicons/favicon.svg" rel="icon" type="image/svg+xml">
        <meta content="#1e2327" name="theme-color">
        <link href="/manifest.json" rel="manifest">
        <div class="position-relative js-header-wrapper">
            <a class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content" href="#start-of-content">Skip to content</a><span class="progress-pjax-loader width-full js-pjax-loader-bar Progress position-fixed"><span class="Progress-item progress-pjax-loader-bar" style="background-color: #79b8ff;width: 0%;"></span></span>
            <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
    
                <div class="container-xl d-lg-flex flex-items-center p-responsive">
    
                    <div class="d-flex flex-justify-between flex-items-center">
                        <a aria-label="Homepage" class="mr-4" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark" href="https://github.com/"><svg aria-hidden="true" class="octicon octicon-mark-github text-white" height="32" version="1.1" viewbox="0 0 16 16" width="32">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg></a>
                        <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
    
                        </div>
                        <div class="d-flex flex-items-center">
                            <a class="d-inline-block d-lg-none f5 text-white no-underline border border-gray-dark rounded-2 px-2 py-1 mr-3 mr-sm-5" data-ga-click="Sign up, click to sign up for account, ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate;ref_cta:Sign up;ref_loc:header logged out" data-hydro-click="" data-hydro-click-hmac="8daadfbd9805d840f27a699224b4231c81310f9721e1337ccc1a5e133854e71f" href="/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&amp;source=header-repo">Sign&nbsp;up</a>  <button aria-expanded="false" aria-label="Toggle navigation" class="btn-link d-lg-none mt-1 js-details-target" type="button"><svg aria-hidden="true" class="octicon octicon-three-bars text-white" height="24" version="1.1" viewbox="0 0 16 16" width="24">
                            <path d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z" fill-rule="evenodd"></path></svg></button>
                        </div>
                    </div>
                    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
    
                        <div class="d-flex d-lg-none flex-justify-end border-bottom bg-gray-light p-3">
                            <button aria-expanded="false" aria-label="Toggle navigation" class="btn-link js-details-target" type="button"><svg aria-hidden="true" class="octicon octicon-x text-gray" height="24" version="1.1" viewbox="0 0 24 24" width="24">
                            <path d="M5.72 5.72a.75.75 0 011.06 0L12 10.94l5.22-5.22a.75.75 0 111.06 1.06L13.06 12l5.22 5.22a.75.75 0 11-1.06 1.06L12 13.06l-5.22 5.22a.75.75 0 01-1.06-1.06L10.94 12 5.72 6.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button>
                        </div>
                        <nav aria-label="Global" class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0">
    
                            <ul class="d-lg-flex list-style-none">
                                <li style="list-style: none"></li>
                                <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
                                    <details class="HeaderMenu-details details-overlay details-reset width-full">
    
                                        <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                                            Why GitHub?<svg class="icon-chevon-down-mktg position-absolute position-lg-relative" viewbox="0 0 14 8" x="0px" y="0px">
                                            <path d="M1,1l6.2,6L13,1"></path></svg>
                                        </summary>
                                        <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                                            <a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features" href="/features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                            <ul class="list-style-none f5 pb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review" href="/features/code-review/">Code review</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management" href="/features/project-management/">Project management</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations" href="/features/integrations">Integrations</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions" href="/features/actions">Actions</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Packages" href="/features/packages">Packages</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Security" href="/features/security">Security</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management" href="/features#team-management">Team management</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting" href="/features#hosting">Hosting</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix hide-xl">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Mobile" href="/mobile">Mobile</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories" href="/customer-stories">Customer stories <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security" href="/security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </details>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3"><a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Team" href="/team">Team</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3"><a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise" href="/enterprise">Enterprise</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
                                    <details class="HeaderMenu-details details-overlay details-reset width-full">
    
                                        <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                                            Explore<svg class="icon-chevon-down-mktg position-absolute position-lg-relative" viewbox="0 0 14 8" x="0px" y="0px">
                                            <path d="M1,1l6.2,6L13,1"></path></svg>
                                        </summary>
                                        <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
    
                                            <ul class="list-style-none mb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore" href="/explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn &amp; contribute</h4>
                                            <ul class="list-style-none mb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics" href="/topics">Topics</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections" href="/collections">Collections</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending" href="/trending">Trending</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab" href="https://lab.github.com/">Learning Lab</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides" href="https://opensource.guide">Open source guides</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
                                            <ul class="list-style-none mb-0">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events" href="https://github.com/events">Events</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum" href="https://github.community">Community forum</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education" href="https://education.github.com">GitHub Education</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Stars Program" href="https://stars.github.com">GitHub Stars program</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </details>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3"><a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace" href="/marketplace">Marketplace</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
                                    <details class="HeaderMenu-details details-overlay details-reset width-full">
    
                                        <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                                            Pricing<svg class="icon-chevon-down-mktg position-absolute position-lg-relative" viewbox="0 0 14 8" x="0px" y="0px">
                                            <path d="M1,1l6.2,6L13,1"></path></svg>
                                        </summary>
                                        <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                                            <a class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing" href="/pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                            <ul class="list-style-none mb-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare plans" href="/pricing#feature-comparison">Compare plans</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Contact Sales" href="https://enterprise.github.com/contact">Contact Sales</a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                            <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits" href="/nonprofit">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                                <li class="edge-item-fix">
                                                    <a class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Education" href="https://education.github.com">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </details>
                                </li>
                                <li style="list-style: none"></li>
                            </ul>
                        </nav>
                        <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
    
                            <div class="d-lg-flex mb-3 mb-lg-0">
    
                                <div aria-expanded="false" aria-haspopup="listbox" aria-label="Search or jump to" aria-owns="jump-to-results" class="header-search header-search-current js-header-search-current flex-auto flex-self-stretch flex-md-self-auto mr-0 mr-md-3 mb-3 mb-md-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to js-header-search-current-jump-to" role="combobox">
    
                                    <div class="position-relative">
                                        <!-- \'"` --><!-- </textarea></xmp> -->
                                        <form accept-charset="UTF-8" action="/CSSEGISandData/COVID-19/search" aria-label="Site" class="js-site-search-form" data-scope-id="238316428" data-scope-type="Repository" data-scoped-search-url="/CSSEGISandData/COVID-19/search" data-unscoped-search-url="/search" method="get" role="search">
                                            <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><input aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search" autocomplete="off" class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable" data-hotkey="s,/" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-scoped-placeholder="Search" data-unscoped-placeholder="Search GitHub" name="q" placeholder="Search" spellcheck="false" type="text" value=""><input class="js-data-jump-to-suggestions-path-csrf" data-csrf="true" type="hidden" value="Fmc6YwmtPQyMav/TxxK81UyJIneQ1Lnu6afZch2ogrRBNSlrEDbtvqQdmkHtf2p8Gmq0riUYhRhgG9pU8QAfcA=="><input class="js-site-search-type-field" name="type" type="hidden"><img alt="" class="mr-2 header-search-key-slash" src="https://github.githubassets.com/images/search-key-slash.svg"></label>
                                            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
                                                <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                <ul class="d-none js-jump-to-suggestions-template-container">
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
                                                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg></label>
                                                    </div> <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28">
                                                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                    </div>
                                                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">In this repository</span> <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">All GitHub</span> <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div>
                                                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">Jump to<span class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div></a> </label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                </ul><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                <ul class="d-none js-jump-to-no-results-template-container">
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span class="text-gray">No suggested jump to results</span></label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                </ul><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                <ul class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container" id="jump-to-results" role="listbox">
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
                                                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg></label>
                                                    </div> <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28">
                                                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                    </div>
                                                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">In this repository</span> <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">All GitHub</span> <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div>
                                                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">Jump to<span class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div></a> </label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
                                                    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16">
                                                        <path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg></label>
                                                    </div> <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28">
                                                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                                    </div>
                                                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"><span aria-label="in this repository" class="js-jump-to-badge-search-text-default d-none">In this repository</span> <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">All GitHub</span> <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div>
                                                    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                                                        <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">Jump to<span class="d-inline-block ml-1 v-align-middle"></span></label>
                                                    </div></a> </label></li>
                                                    <li style="list-style: none"><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label></li>
                                                </ul><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                            </div><label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container"></label>
                                        </form>
                                    </div>
                                </div>
                            </div> <a class="HeaderMenu-link no-underline mr-3" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in" data-hydro-click="" data-hydro-click-hmac="453f406786f8ed65267f5f57d2c31b709c558aa9409ca1a988f71d251a3ee64b" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19%2Ftree%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_daily_reports">Sign&nbsp;in</a> <a class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1" data-ga-click="Sign up, click to sign up for account, ref_page:/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate;ref_cta:Sign up;ref_loc:header logged out" data-hydro-click="" data-hydro-click-hmac="453f406786f8ed65267f5f57d2c31b709c558aa9409ca1a988f71d251a3ee64b" href="/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&amp;source=header-repo&amp;source_repo=CSSEGISandData%2FCOVID-19">Sign&nbsp;up</a>
                        </div>
                    </div>
                </div>
            </header>
        </div>
        <div class="show-on-focus" id="start-of-content"></div>
        <div id="js-flash-container">
    
            <template class="js-flash-template">
    
                <div class="flash flash-full {{ className }}">
    
                    <div class=" px-2">
                        <button aria-label="Dismiss this message" class="flash-close js-flash-close" type="button"><svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                        <path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button>
                        <div>
                            {{ message }}
                        </div>
                    </div>
                </div>
            </template>
        </div>
        <div class="application-main">
    
            <div class="" itemscope itemtype="http://schema.org/SoftwareSourceCode">
    
                <main data-pjax-container="" id="js-repo-pjax-container">
                    <div class="bg-gray-light pt-3 hide-full-screen mb-5">
    
                        <div class="d-flex mb-3 px-3 px-md-4 px-lg-5">
    
                            <div class="flex-auto min-width-0 width-fit mr-3">
    
                                <h1 class=" d-flex flex-wrap flex-items-center break-word f3 text-normal"><svg aria-hidden="true" class="octicon octicon-repo text-gray" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg><span class="author ml-2 flex-self-stretch" itemprop="author"><a class="url fn" data-hovercard-type="user" data-hovercard-url="/users/CSSEGISandData/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/CSSEGISandData" rel="author">CSSEGISandData</a></span> <span class="mx-1 flex-self-stretch">/</span><strong class="mr-2 flex-self-stretch" itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/CSSEGISandData/COVID-19">COVID-19</a></strong> </h1>
                            </div>
                            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
                                <li style="list-style: none"></li>
                                <li><a aria-label="You must be signed in to watch a repository" class="tooltipped tooltipped-s btn btn-sm btn-with-count" data-hydro-click="" data-hydro-click-hmac="8bcf781b787d7a363448427b5e6be6e4bba67f0bb4d18bbe9540c2662563d229" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19" rel="nofollow"><svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z" fill-rule="evenodd"></path></svg>Watch</a> <a aria-label="911 users are watching this repository" class="social-count" href="/CSSEGISandData/COVID-19/watchers">911</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li><a aria-label="You must be signed in to star a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click="" data-hydro-click-hmac="ef2e47d75f6298a99bda8c34181197c7e0663581b1beefbf78bbd5d351aef126" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19" rel="nofollow"><svg aria-hidden="true" class="octicon octicon-star v-align-text-bottom" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" fill-rule="evenodd"></path></svg>Star</a><a aria-label="23842 users starred this repository" class="social-count js-social-count" href="/CSSEGISandData/COVID-19/stargazers">23.8k</a>
                                </li>
                                <li style="list-style: none"></li>
                                <li><a aria-label="You must be signed in to fork a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click="" data-hydro-click-hmac="b27e52197fadff8c461ad531c53f1a66acc46a4ec178ce946976f83749e056e4" href="/login?return_to=%2FCSSEGISandData%2FCOVID-19" rel="nofollow"><svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z" fill-rule="evenodd"></path></svg>Fork</a><a aria-label="14983 users forked this repository" class="social-count" href="/CSSEGISandData/COVID-19/network/members">15k</a>
                                </li>
                                <li style="list-style: none"></li>
                            </ul>
                        </div>
                        <nav aria-label="Repository" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5 bg-gray-light" data-pjax="#js-repo-pjax-container">
    
                            <ul class="UnderlineNav-body list-style-none">
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item selected UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Code tab" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /CSSEGISandData/COVID-19" data-tab-item="code-tab" href="/CSSEGISandData/COVID-19"><svg aria-hidden="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z" fill-rule="evenodd"></path></svg><span data-content="Code">Code</span><span class="Counter" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Issues tab" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /CSSEGISandData/COVID-19/issues" data-tab-item="issues-tab" href="/CSSEGISandData/COVID-19/issues"><svg aria-hidden="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" fill-rule="evenodd"></path></svg><span data-content="Issues">Issues</span><span class="Counter" title="1,307">1.3k</span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Pull requests tab" data-hotkey="g p" data-selected-links="repo_pulls checks /CSSEGISandData/COVID-19/pulls" data-tab-item="pull-requests-tab" href="/CSSEGISandData/COVID-19/pulls"><svg aria-hidden="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z" fill-rule="evenodd"></path></svg><span data-content="Pull requests">Pull requests</span><span class="Counter" title="273">273</span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Actions tab" data-hotkey="g a" data-selected-links="repo_actions /CSSEGISandData/COVID-19/actions" data-tab-item="actions-tab" href="/CSSEGISandData/COVID-19/actions"><svg aria-hidden="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z" fill-rule="evenodd"></path></svg><span data-content="Actions">Actions</span><span class="Counter" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Projects tab" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /CSSEGISandData/COVID-19/projects" data-tab-item="projects-tab" href="/CSSEGISandData/COVID-19/projects"><svg aria-hidden="true" class="octicon octicon-project UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg><span data-content="Projects">Projects</span><span class="Counter" hidden="hidden" title="0">0</span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Security tab" data-hotkey="g s" data-selected-links="security overview alerts policy token_scanning code_scanning /CSSEGISandData/COVID-19/security" data-tab-item="security-tab" href="/CSSEGISandData/COVID-19/security"><svg aria-hidden="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z" fill-rule="evenodd"></path></svg><span data-content="Security">Security</span><span class="js-security-tab-count Counter" data-url="/CSSEGISandData/COVID-19/security/overall-count" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                                <li class="d-flex"><a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-ga-click="Repository, Navigation click, Insights tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people /CSSEGISandData/COVID-19/pulse" data-tab-item="insights-tab" href="/CSSEGISandData/COVID-19/pulse"><svg aria-hidden="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z" fill-rule="evenodd"></path></svg><span data-content="Insights">Insights</span><span class="Counter" title="Not available"></span></a>
                                </li>
                                <li style="list-style: none"></li>
                            </ul>
                            <div class="position-absolute right-0 pr-3 pr-md-4 pr-lg-5 js-responsive-underlinenav-overflow" style="visibility:hidden;">
    
                                <details class="details-overlay details-reset position-relative">
    
                                    <summary role="button">
    
                                    </summary>
                                    <div class="UnderlineNav-item mr-0 border-0">
                                        <svg aria-hidden="true" class="octicon octicon-kebab-horizontal" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                        <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg><span class="sr-only">More</span>
                                    </div>
                                    <ul>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="code-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19" href="/CSSEGISandData/COVID-19" role="menuitem">Code</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="issues-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/issues" href="/CSSEGISandData/COVID-19/issues" role="menuitem">Issues</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="pull-requests-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/pulls" href="/CSSEGISandData/COVID-19/pulls" role="menuitem">Pull requests</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="actions-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/actions" href="/CSSEGISandData/COVID-19/actions" role="menuitem">Actions</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="projects-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/projects" href="/CSSEGISandData/COVID-19/projects" role="menuitem">Projects</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="security-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/security" href="/CSSEGISandData/COVID-19/security" role="menuitem">Security</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                        <li data-menu-item="insights-tab" hidden=""><a class="js-selected-navigation-item dropdown-item" data-selected-links=" /CSSEGISandData/COVID-19/pulse" href="/CSSEGISandData/COVID-19/pulse" role="menuitem">Insights</a>
                                        </li>
                                        <li style="list-style: none"></li>
                                    </ul>
                                </details>
                            </div>
                        </nav>
                    </div>
                    <div class="container-xl clearfix new-discussion-timeline px-3 px-md-4 px-lg-5">
    
                        <div class="repository-content">
    
                            <div class="file-navigation mb-3 d-flex flex-items-start">
    
                                <div class="position-relative">
    
                                    <details class="details-reset details-overlay mr-0 mb-0" id="branch-select-menu">
    
                                        <summary class="btn css-truncate" data-hotkey="w" title="Switch branches or tags">
                                            <svg aria-hidden="true" class="octicon octicon-git-branch text-gray" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                            <path d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z" fill-rule="evenodd"></path></svg><span class="css-truncate-target" data-menu-button="">master</span><span class="dropdown-caret"></span>
                                        </summary>
                                        <div class="SelectMenu-modal">
                                             <svg aria-hidden="true" class="octicon octicon-octoface anim-pulse" height="32" version="1.1" viewbox="0 0 24 24" width="32">
                                            <path d="M7.75 11c-.69 0-1.25.56-1.25 1.25v1.5a1.25 1.25 0 102.5 0v-1.5C9 11.56 8.44 11 7.75 11zm1.27 4.5a.469.469 0 01.48-.5h5a.47.47 0 01.48.5c-.116 1.316-.759 2.5-2.98 2.5s-2.864-1.184-2.98-2.5zm7.23-4.5c-.69 0-1.25.56-1.25 1.25v1.5a1.25 1.25 0 102.5 0v-1.5c0-.69-.56-1.25-1.25-1.25z"></path>
                                            <path d="M21.255 3.82a1.725 1.725 0 00-2.141-1.195c-.557.16-1.406.44-2.264.866-.78.386-1.647.93-2.293 1.677A18.442 18.442 0 0012 5c-.93 0-1.784.059-2.569.17-.645-.74-1.505-1.28-2.28-1.664a13.876 13.876 0 00-2.265-.866 1.725 1.725 0 00-2.141 1.196 23.645 23.645 0 00-.69 3.292c-.125.97-.191 2.07-.066 3.112C1.254 11.882 1 13.734 1 15.527 1 19.915 3.13 23 12 23c8.87 0 11-3.053 11-7.473 0-1.794-.255-3.647-.99-5.29.127-1.046.06-2.15-.066-3.125a23.652 23.652 0 00-.689-3.292zM20.5 14c.5 3.5-1.5 6.5-8.5 6.5s-9-3-8.5-6.5c.583-4 3-6 8.5-6s7.928 2 8.5 6z" fill-rule="evenodd"></path></svg>
                                        </div>
                                    </details>
                                </div>
                                <div class="flex-1 mx-2 flex-self-center f4">
    
                                    <div class="d-none d-sm-block">
                                        <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19"><span>COVID-19</span></a></span></span><span class="mx-1">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data"><span>csse_covid_19_data</span></a></span><span class="mx-1">/</span><strong class="final-path">csse_covid_19_daily_reports</strong><span class="mx-1">/</span>
                                    </div>
                                </div>
                                <div class="d-flex">
                                    <a class="btn mr-2 d-none d-md-block" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-hydro-click="" data-hydro-click-hmac="f69eeff120eac2d87ab515142f9599079e40e011adadb6a8a0e21f336af95f93" data-pjax="true" href="/CSSEGISandData/COVID-19/find/master">Go to file</a>
                                </div>
                            </div>
                            <div class="f4 mt-3 mb-3 d-sm-none">
                                <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19"><span>COVID-19</span></a></span></span><span class="mx-1">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data"><span>csse_covid_19_data</span></a></span><span class="mx-1">/</span><strong class="final-path">csse_covid_19_daily_reports</strong><span class="separator mx-1">/</span>
                            </div>
                            <div class="Box mb-3">
    
                                <div class="Box-header Box-header--blue position-relative">
    
                                    <h2 class="sr-only">Latest commit</h2>
                                    <div class="js-details-container Details d-flex rounded-top-1 flex-items-center flex-wrap" data-issue-and-pr-hovercards-enabled="">
    
                                        <div class="flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1 hx_avatar_stack_commit">
    
                                            <div class="AvatarStack flex-self-start">
    
                                                <div aria-label="CSSEGISandData" class="AvatarStack-body">
                                                    <a class="avatar avatar-user" data-hovercard-type="user" data-hovercard-url="/users/CSSEGISandData/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" data-skip-pjax="true" href="/CSSEGISandData" style="width:24px;height:24px;"><img alt="@CSSEGISandData" class=" avatar-user" height="24" src="https://avatars1.githubusercontent.com/u/60674295?s=60&amp;u=cda3e09cda856b17dbc71dbd50b87f75955e7e48&amp;v=4" width="24"></a>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="flex-1 d-flex flex-items-center ml-3 min-width-0">
    
                                            <div class="css-truncate css-truncate-overflow text-gray">
                                                 <a class="commit-author user-mention" href="/CSSEGISandData/COVID-19/commits?author=CSSEGISandData" title="View all commits by CSSEGISandData">CSSEGISandData</a> <span class="d-none d-sm-inline"><a class="link-gray-dark" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6" title="Automated update">Automated update</a></span>
                                            </div><span class="hidden-text-expander ml-2 d-inline-block d-inline-block d-lg-none"><button aria-expanded="false" class="hx_bg-black-fade-15 text-gray-dark ellipsis-expander js-details-target" type="button"><span class="hidden-text-expander ml-2 d-inline-block d-inline-block d-lg-none">&hellip;</span></button></span>
                                            <div class="d-flex flex-auto flex-justify-end ml-3 flex-items-baseline">
                                                 <a class="f6 link-gray text-mono ml-2 d-none d-lg-inline" data-pjax="" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6">0bf4d22</a><a class="link-gray ml-2" data-pjax="" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6">Sep 8, 2020</a>
                                            </div>
                                        </div>
                                        <div class="pl-0 pl-md-5 flex-order-1 width-full Details-content--hidden">
    
                                            <div class="mt-2">
                                                <a class="link-gray-dark text-bold" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/0bf4d22e5205622c14962f27d596c067086a4dc6">Automated update</a>
                                            </div>
                                            <div class="d-flex flex-items-center">
                                                <span class="text-gray-dark text-mono d-lg-none hx_bg-black-fade-15 px-1 rounded-1 text-small mt-2">0bf4d22</span>
                                            </div>
                                        </div>
                                        <div class="flex-shrink-0">
    
                                            <h2 class="sr-only">Git stats</h2>
                                            <ul class="list-style-none d-flex">
                                                <li style="list-style: none"></li>
                                                <li class="ml-0 ml-md-3"><a class="pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 link-gray-dark no-underline no-wrap" data-pjax="" href="/CSSEGISandData/COVID-19/commits/master/csse_covid_19_data/csse_covid_19_daily_reports"><svg aria-hidden="true" class="octicon octicon-history text-gray" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                                    <path d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z" fill-rule="evenodd"></path></svg><span class="d-none d-sm-inline"><strong>History</strong></span> </a>
                                                </li>
                                                <li style="list-style: none"></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                                <h2 class="sr-only" id="files">Files</h2><a class="d-none js-permalink-shortcut" data-hotkey="y" href="/CSSEGISandData/COVID-19/tree/0bf4d22e5205622c14962f27d596c067086a4dc6/csse_covid_19_data/csse_covid_19_daily_reports">Permalink</a>
                                <div class="flash flash-full flash-error include-fragment-error py-2">
                                    <svg aria-hidden="true" class="octicon octicon-alert mr-2" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                                    <path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg> Failed to load latest commit information.
                                </div>
                                <div class="js-details-container Details">
    
                                    <div aria-labelledby="files" class="Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-block" data-pjax="" role="grid">
    
                                        <div class="sr-only" role="row">
    
                                            <div role="columnheader">
                                                Type
                                            </div>
                                            <div role="columnheader">
                                                Name
                                            </div>
                                            <div class="d-none d-md-block" role="columnheader">
                                                Latest commit message
                                            </div>
                                            <div role="columnheader">
                                                Commit time
                                            </div>
                                        </div>
                                        <div class="Box-row Box-row--focus-gray p-0 d-flex js-navigation-item" role="row">
    
                                            <div class="flex-auto min-width-0 col-md-2" role="rowheader">
                                                <a class="js-navigation-open d-block py-2 px-3" href="/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data" rel="nofollow" title="Go to parent directory"><span class="text-bold text-center d-inline-block" style="min-width: 16px;">. .</span></a>
                                            </div>
                                            <div class="d-none d-md-block" role="gridcell"></div>
                                            <div role="gridcell"></div>
                                        </div>
                                        <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
    
                                            <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
                                                <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
                                                <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
                                            </div>
                                            <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/.gitignore" id="a084b794bc0759e7a6b77810e01874f2-496ee2ca6a2f08396a4076fe43dedf3dc0da8b6d" title=".gitignore">.gitignore</a></span>
                                            </div>
                                            <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/ddd8cf43bd6a3c40d12f48668f5ea39e7c42f708" title="update">update</a></span>
                                            </div>
                                            <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
                                                Feb 14, 2020
                                            </div>
                                        </div>
                                        {four_csv_links}
                                        <div class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item" role="row">
    
                                            <div class="mr-3 flex-shrink-0" role="gridcell" style="width: 16px;">
                                                <svg aria-label="File" class="octicon octicon-file text-gray-light" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16">
                                                <path d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z" fill-rule="evenodd"></path></svg>
                                            </div>
                                            <div class="flex-auto min-width-0 col-md-2 mr-3" role="rowheader">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open link-gray-dark" href="/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/README.md" id="04c6e90faac2675aa89e2176d2eec7d8-e69de29bb2d1d6434b8b29ae775ad8c2e48c5391" title="README.md">README.md</a></span>
                                            </div>
                                            <div class="flex-auto min-width-0 d-none d-md-block col-5 mr-3 commit-message" role="gridcell">
                                                <span class="css-truncate css-truncate-target d-block width-fit"><a class="link-gray" data-pjax="true" href="/CSSEGISandData/COVID-19/commit/7e3dbcde3f44c7a312d3bd010cbe36fa609dd869" title="update">update</a></span>
                                            </div>
                                            <div class="text-gray-light text-right" role="gridcell" style="width:100px;">
                                                Feb 14, 2020
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
        <div class="footer container-xl width-full p-responsive" role="contentinfo">
    
            <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light">
    
                <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to status, text:status" href="https://githubstatus.com/">Status</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li>
                        <a data-ga-click="Footer, go to help, text:help" href="https://docs.github.com">Help</a>
                    </li>
                    <li style="list-style: none"></li>
                </ul> <a aria-label="Homepage" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com" title="GitHub"><svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewbox="0 0 16 16" width="24">
                <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg></a>
                <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to Pricing, text:Pricing" href="https://github.com/pricing">Pricing</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to api, text:api" href="https://docs.github.com">API</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to training, text:training" href="https://services.github.com">Training</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li class="mr-3 mr-lg-0">
                        <a data-ga-click="Footer, go to blog, text:blog" href="https://github.blog">Blog</a>
                    </li>
                    <li style="list-style: none"></li>
                    <li>
                        <a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a>
                    </li>
                    <li style="list-style: none"></li>
                </ul>
            </div>
            <div class="d-flex flex-justify-center pb-6">
                <span class="f6 text-gray-light"></span>
            </div>
        </div>
        <div class="ajax-error-message flash flash-error" id="ajax-error-message">
            <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg><button aria-label="Dismiss error" class="flash-close js-ajax-error-dismiss" type="button"><svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button> You can perform that action at this time.
        </div>
        <script async="async" data-src="https://github.githubassets.com/assets/compat-bootstrap-6e7ff7ac.js" id="js-conditional-compat" type="application/javascript">
        </script>
        <script src="https://github.githubassets.com/assets/environment-bootstrap-0b18da31.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/vendor-d2216e0f.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/frameworks-708fa234.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/behaviors-bootstrap-08dae8c4.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/contributions-spider-graph-36a4ea81.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./drag-drop.js" data-src="https://github.githubassets.com/assets/drag-drop-ad7fde7d.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./image-crop-element-loader.js" data-src="https://github.githubassets.com/assets/image-crop-element-loader-88bb82db.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./jump-to.js" data-src="https://github.githubassets.com/assets/jump-to-402b99bd.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./profile-pins-element.js" data-src="https://github.githubassets.com/assets/profile-pins-element-1f359478.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./randomColor.js" data-src="https://github.githubassets.com/assets/randomColor-a840affe.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./sortable-behavior.js" data-src="https://github.githubassets.com/assets/sortable-behavior-bcaeeb46.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./tweetsodium.js" data-src="https://github.githubassets.com/assets/tweetsodium-987aac13.js" type="application/javascript">
        </script>
        <script async="async" data-module-id="./user-status-submit.js" data-src="https://github.githubassets.com/assets/user-status-submit-eb836b74.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/repositories-dd933f65.js" type="application/javascript">
        </script>
        <script async="async" src="https://github.githubassets.com/assets/github-bootstrap-83b909b4.js" type="application/javascript">
        </script>
        <div class="js-stale-session-flash flash flash-warn flash-banner">
            <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16">
            <path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg><span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span><span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
        </div>
        <template id="site-details-dialog">
    
            <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open="">
    
                <summary aria-label="Close dialog" role="button"></summary> <button aria-label="Close dialog" class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" data-close-dialog="" type="button"><svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16">
                <path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg></button>
                <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
            </details>
        </template>
        <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
    
            <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
    
            </div>
        </div>
    </body>
    </html>
"""
