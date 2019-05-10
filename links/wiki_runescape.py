from bs4 import BeautifulSoup


html = """
<!DOCTYPE html><html class="client-nojs" lang="en-GB" dir="ltr"><head><script async src="https://www.googletagmanager.com/gtag/js?id=UA-126479006-1"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","UA-126479006-1");</script><meta charset="UTF-8"/><title>Bestiary/Levels 1 to 10 - OSRS Wiki</title><script>document.documentElement.className=document.documentElement.className.replace( /(^|\s)client-nojs(\s|$)/, "$1client-js$2" );</script><script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Bestiary/Levels_1_to_10","wgTitle":"Bestiary/Levels 1 to 10","wgCurRevisionId":8108670,"wgRevisionId":8108670,"wgArticleId":18182,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Bestiary"],"wgBreakFrames":false,"wgPageContentLanguage":"en-gb","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"Bestiary/Levels_1_to_10","wgRelevantArticleId":18182,"wgRequestId":"82a5027f943241d8a81a8634e5df3cae","wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgWikiEditorEnabledModules":[],"wgVisualEditor":{"pageLanguageCode":"en-GB","pageLanguageDir":"ltr","pageVariantFallbacks":"en-gb","usePageImages":true,"usePageDescriptions":false},"wgPreferredVariant":"en-gb","wgMFExpandAllSectionsUserOption":true,"wgMFEnableFontChanger":true,"wgMFDisplayWikibaseDescriptions":{"search":false,"nearby":false,"watchlist":false,"tagline":false},"wgPopupsShouldSendModuleToUser":true,"wgPopupsConflictsWithNavPopupGadget":false,"simpleBatchUploadMaxFilesPerBatch":{"*":1000},"wgVisualEditorToolbarScrollOffset":0,"wgVisualEditorUnsupportedEditParams":["undo","undoafter","veswitched"],"wgEditSubmitButtonLabelPublish":false,"wgCodeMirrorEnabled":true,"wgSiteNoticeId":"1.1"});mw.loader.state({"site.styles":"ready","noscript":"ready","user.styles":"ready","user":"ready","site":"ready","user.options":"loading","user.tokens":"loading","ext.cite.styles":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.smw.style":"ready","ext.smw.tooltip.styles":"ready","ext.dismissableSiteNotice.styles":"ready","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","mediawiki.sectionAnchor":"ready","mediawiki.skinning.interface":"ready","skins.vector.styles":"ready"});mw.loader.implement("user.options@0qpjoud",function($,jQuery,require,module){/*@nomin*/mw.user.options.set({"variant":"en-gb"});});mw.loader.implement("user.tokens@14p3yrv",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"editToken":"+\","patrolToken":"+\","watchToken":"+\","csrfToken":"+\"});});mw.loader.load(["ext.smw.style","ext.smw.tooltips","ext.cite.a11y","mediawiki.page.startup","mediawiki.user","mediawiki.hidpi","mediawiki.page.ready","jquery.makeCollapsible","mediawiki.toc","mediawiki.searchSuggest","ext.gadget.rsw-util","ext.gadget.switchInfobox","ext.gadget.parentheses","ext.gadget.GECharts","ext.gadget.exchangePages","ext.gadget.compare","ext.gadget.gemwupdate","ext.gadget.youtube","ext.gadget.autosort","ext.gadget.highlightTable","ext.gadget.titleparenthesis","ext.gadget.topIcons","ext.gadget.Username","ext.gadget.countdown","ext.gadget.autocollapse","ext.gadget.checkboxList","ext.gadget.calc","ext.gadget.monstercalc","ext.gadget.infoboxQty","ext.gadget.calculatorNS","ext.gadget.dropDisplay","ext.gadget.contributions","ext.gadget.skinTogglesNew","ext.gadget.utcclock","ext.gadget.relativetime","ext.gadget.navboxToggle","ext.gadget.dropdown","ext.gadget.newPage","ext.gadget.purge","ext.gadget.ReferenceTooltips","ext.gadget.fileDownload","ext.gadget.sigreminder","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.popups","skins.vector.js","ext.dismissableSiteNotice"]);});</script><link rel="stylesheet" href="/load.php?debug=false&amp;lang=en-gb&amp;modules=ext.cite.styles%7Cext.dismissableSiteNotice.styles%7Cext.visualEditor.desktopArticleTarget.noscript%7Cmediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.sectionAnchor%7Cmediawiki.skinning.interface%7Cskins.vector.styles&amp;only=styles&amp;skin=vector"/><link rel="stylesheet" href="/load.php?debug=false&amp;lang=en-gb&amp;modules=ext.smw.style%7Cext.smw.tooltip.styles&amp;only=styles&amp;skin=vector"/><script async="" src="/load.php?debug=false&amp;lang=en-gb&amp;modules=startup&amp;only=scripts&amp;skin=vector"></script><meta name="ResourceLoaderDynamicStyles" content=""/><link rel="stylesheet" href="/load.php?debug=false&amp;lang=en-gb&amp;modules=site.styles&amp;only=styles&amp;skin=vector"/><meta name="generator" content="MediaWiki 1.31.1"/><link rel="alternate" type="application/rdf+xml" title="Bestiary/Levels 1 to 10" href="/w/Special:ExportRDF/Bestiary/Levels_1_to_10?xmlmime=rdf"/><link rel="alternate" type="application/x-wiki" title="Edit" href="/w/Bestiary/Levels_1_to_10?action=edit"/><link rel="edit" title="Edit" href="/w/Bestiary/Levels_1_to_10?action=edit"/><link rel="apple-touch-icon" href="/images/4/43/Apple-touch-icon.png"/><link rel="search" type="application/opensearchdescription+xml" href="/opensearch_desc.php" title="Old School RuneScape Wiki (en-gb)"/><link rel="EditURI" type="application/rsd+xml" href="//oldschool.runescape.wiki/api.php?action=rsd"/><link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/3.0/"/><link rel="canonical" href="https://oldschool.runescape.wiki/w/Bestiary/Levels_1_to_10"/><meta property="og:type" content="article"/><meta property="og:site_name" content="Old School RuneScape Wiki"/><meta property="og:title" content="Bestiary/Levels 1 to 10"/><meta property="og:url" content="//oldschool.runescape.wiki/w/Bestiary/Levels_1_to_10"/></head><body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Bestiary_Levels_1_to_10 rootpage-Bestiary skin-vector action-view"><div id="mw-page-base" class="noprint"></div><div id="mw-head-base" class="noprint"></div><div id="content" class="mw-body" role="main"><a id="top"></a><div id="siteNotice" class="mw-body-content"><div id="mw-dismissablenotice-anonplace"></div><script>(function(){var node=document.getElementById("mw-dismissablenotice-anonplace");if(node){node.outerHTML="\u003Cdiv class="mw-dismissable-notice"\u003E\u003Cdiv class="mw-dismissable-notice-close"\u003E[\u003Ca href="#"\u003Edismiss\u003C/a\u003E]\u003C/div\u003E\u003Cdiv class="mw-dismissable-notice-body"\u003E\u003Cdiv id="localNotice" lang="en-GB" dir="ltr"\u003E\u003Cdiv class="mw-parser-output"\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E\u003C/div\u003E";}}());</script></div><div class="mw-indicators mw-body-content"></div><h1 id="firstHeading" class="firstHeading" lang="en-GB">Bestiary/Levels 1 to 10</h1><div id="bodyContent" class="mw-body-content"><div id="siteSub" class="noprint">From Old School RuneScape Wiki</div><div id="contentSub"><span class="subpages">&lt; <a href="/w/Bestiary" title="Bestiary">Bestiary</a></span></div><div id="jump-to-nav" class="mw-jump">Jump to:<a href="#mw-head">navigation</a>, <a href="#p-search">search</a></div><div id="mw-content-text" lang="en-GB" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><div id="toc" class="toc"><div class="toctitle" lang="en-GB" dir="ltr"><h2>Contents</h2></div><ul><li class="toclevel-1 tocsection-1"><a href="#Level_1"><span class="tocnumber">1</span> <span class="toctext">Level 1</span></a></li><li class="toclevel-1 tocsection-2"><a href="#Level_2"><span class="tocnumber">2</span> <span class="toctext">Level 2</span></a></li><li class="toclevel-1 tocsection-3"><a href="#Level_3"><span class="tocnumber">3</span> <span class="toctext">Level 3</span></a></li><li class="toclevel-1 tocsection-4"><a href="#Level_4"><span class="tocnumber">4</span> <span class="toctext">Level 4</span></a></li><li class="toclevel-1 tocsection-5"><a href="#Level_5"><span class="tocnumber">5</span> <span class="toctext">Level 5</span></a></li><li class="toclevel-1 tocsection-6"><a href="#Level_6"><span class="tocnumber">6</span> <span class="toctext">Level 6</span></a></li><li class="toclevel-1 tocsection-7"><a href="#Level_7"><span class="tocnumber">7</span> <span class="toctext">Level 7</span></a></li><li class="toclevel-1 tocsection-8"><a href="#Level_8"><span class="tocnumber">8</span> <span class="toctext">Level 8</span></a></li><li class="toclevel-1 tocsection-9"><a href="#Level_9"><span class="tocnumber">9</span> <span class="toctext">Level 9</span></a></li><li class="toclevel-1 tocsection-10"><a href="#Level_10"><span class="tocnumber">10</span> <span class="toctext">Level 10</span></a></li><li class="toclevel-1 tocsection-11"><a href="#References"><span class="tocnumber">11</span> <span class="toctext">References</span></a></li></ul></div><h3><span class="mw-headline" id="Level_1">Level 1</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=1&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 1">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=1" title="Edit section: Level 1">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Chicken" title="Chicken">Chicken</a><sup id="cite_ref-g_1-0" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Drake_(bird)" title="Drake (bird)">Drake</a></li><li><a href="/w/Duck" title="Duck">Duck</a></li><li><a href="/w/Duckling" title="Duckling">Duckling</a></li><li><a href="/w/Gnome" title="Gnome">Gnome</a></li><li><a href="/w/Gnome_troop" title="Gnome troop">Gnome troop</a></li><li><a href="/w/Rat" title="Rat">Rat</a><sup id="cite_ref-g_1-1" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Solus_Dellagar" title="Solus Dellagar">Solus Dellagar</a></li><li><a href="/w/Spider" title="Spider">Spider</a><sup id="cite_ref-g_1-2" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Undead_chicken" title="Undead chicken">Undead chicken</a><sup id="cite_ref-g_1-3" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li></ul><h3><span class="mw-headline" id="Level_2">Level 2</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=2&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 2">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=2" title="Edit section: Level 2">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Anja" title="Anja">Anja</a></li><li><a href="/w/Carnivorous_chinchompa" title="Carnivorous chinchompa">Carnivorous chinchompa</a></li><li><a href="/w/Cow" title="Cow">Cow</a><sup id="cite_ref-g_1-4" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Cow_calf" title="Cow calf">Cow calf</a></li><li><a href="/w/Entrana_firebird" title="Entrana firebird">Entrana firebird</a></li><li><a href="/w/Giant_spider" title="Giant spider">Giant spider</a></li><li><a href="/w/Goblin" title="Goblin">Goblin</a></li><li><a href="/w/Hengel" title="Hengel">Hengel</a></li><li><a href="/w/Imp" title="Imp">Imp</a></li><li><a href="/w/Jeff" title="Jeff">Jeff</a></li><li><a href="/w/Johnny_the_Beard" class="mw-redirect" title="Johnny the Beard">Johnny the Beard</a></li><li><a href="/w/Man" title="Man">Man</a></li><li><a href="/w/Narf" title="Narf">Narf</a></li><li><a href="/w/Penguin" title="Penguin">Penguin</a></li><li><a href="/w/Rabbit" title="Rabbit">Rabbit</a></li><li><a href="/w/Rusty" title="Rusty">Rusty</a></li><li><a href="/w/Seagull" title="Seagull">Seagull</a></li><li><a href="/w/Tramp" title="Tramp">Tramp</a></li><li><a href="/w/Undead_cow" title="Undead cow">Undead cow</a><sup id="cite_ref-g_1-5" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Woman" title="Woman">Woman</a></li><li><a href="/w/Wormbrain" title="Wormbrain">Wormbrain</a></li></ul><h3><span class="mw-headline" id="Level_3">Level 3</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=3&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 3">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=3" title="Edit section: Level 3">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Cave_goblin_(monster)" title="Cave goblin (monster)">Cave goblin</a><sup id="cite_ref-g_1-6" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Cuffs" title="Cuffs">Cuffs</a></li><li><a href="/w/Drunken_man" title="Drunken man">Drunken man</a></li><li><a href="/w/Gardener" title="Gardener">Gardener</a></li><li><a href="/w/Giant_rat" title="Giant rat">Giant rat</a><sup id="cite_ref-g_1-7" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Monkey" title="Monkey">Monkey</a></li><li><a href="/w/Seagull" title="Seagull">Seagull</a></li><li><a href="/w/Wyson" class="mw-redirect" title="Wyson">Wyson</a></li><li><a href="/w/Zombie_rat" title="Zombie rat">Zombie rat</a></li></ul><h3><span class="mw-headline" id="Level_4">Level 4</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=4&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 4">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=4" title="Edit section: Level 4">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Ceolburg" title="Ceolburg">Ceolburg</a></li><li><a href="/w/Gardener" title="Gardener">Gardener</a></li><li><a href="/w/Hygd" title="Hygd">Hygd</a></li></ul><h3><span class="mw-headline" id="Level_5">Level 5</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=5&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 5">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=5" title="Edit section: Level 5">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Frog" title="Frog">Frog</a></li><li><a href="/w/Bird" title="Bird">Bird</a></li><li><a href="/w/Desert_snake" title="Desert snake">Desert snake</a></li><li><a href="/w/Goblin" title="Goblin">Goblin</a><sup id="cite_ref-g_1-8" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Highwayman" title="Highwayman">Highwayman</a></li><li><a href="/w/Monk" title="Monk">Monk</a></li><li><a href="/w/Snake" title="Snake">Snake</a></li></ul><h3><span class="mw-headline" id="Level_6">Level 6</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=6&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 6">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=6" title="Edit section: Level 6">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Bat" title="Bat">Bat</a></li><li><a href="/w/Cave_bug" title="Cave bug">Cave bug</a></li><li><a href="/w/Chompy_bird" title="Chompy bird">Chompy bird</a></li><li><a href="/w/Giant_rat" title="Giant rat">Giant rat</a><sup id="cite_ref-g_1-9" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li><li><a href="/w/Mugger" title="Mugger">Mugger</a><sup id="cite_ref-g_1-10" class="reference"><a href="#cite_note-g-1">&#91;1&#93;</a></sup></li></ul><h3><span class="mw-headline" id="Level_7">Level 7</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=7&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 7">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=7" title="Edit section: Level 7">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Dark_wizard" title="Dark wizard">Dark wizard</a></li><li><a href="/w/Dwarf" title="Dwarf">Dwarf</a></li><li><a href="/w/Farmer" title="Farmer">Farmer</a></li></ul><h3><span class="mw-headline" id="Level_8">Level 8</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=8&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 8">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=8" title="Edit section: Level 8">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Crawling_Hand" title="Crawling Hand">Crawling Hand</a></li><li><a href="/w/Dark_warrior" title="Dark warrior">Dark warrior</a></li></ul><h3><span class="mw-headline" id="Level_9">Level 9</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=9&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 9">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=9" title="Edit section: Level 9">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Al-Kharid_warrior" title="Al-Kharid warrior">Al-Kharid warrior</a></li><li><a href="/w/Barbarian" title="Barbarian">Barbarian</a></li><li><a href="/w/Myre_Blamish_Snail" title="Myre Blamish Snail">Myre Blamish Snail</a></li><li><a href="/w/Wizard" title="Wizard">Wizard</a></li></ul><h3><span class="mw-headline" id="Level_10">Level 10</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=10&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: Level 10">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=10" title="Edit section: Level 10">edit source</a><span class="mw-editsection-bracket">]</span></span></h3><ul><li><a href="/w/Barbarian" title="Barbarian">Barbarian</a></li><li><a href="/w/Dwarf" title="Dwarf">Dwarf</a></li><li><a href="/w/Ochre_Blamish_Snail" title="Ochre Blamish Snail">Ochre Blamish Snail</a></li><li><a href="/w/Rowdy_slave" title="Rowdy slave">Rowdy slave</a></li><li><a href="/w/Thug" title="Thug">Thug</a></li></ul><h2><span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/Bestiary/Levels_1_to_10?section=11&amp;veaction=edit" class="mw-editsection-visualeditor" title="Edit section: References">edit</a><span class="mw-editsection-divider"> | </span><a href="/w/Bestiary/Levels_1_to_10?action=edit&amp;section=11" title="Edit section: References">edit source</a><span class="mw-editsection-bracket">]</span></span></h2><div class="mw-references-wrap"><ol class="references"><li id="cite_note-g-1"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-g_1-0">1.00</a></sup> <sup><a href="#cite_ref-g_1-1">1.01</a></sup> <sup><a href="#cite_ref-g_1-2">1.02</a></sup> <sup><a href="#cite_ref-g_1-3">1.03</a></sup> <sup><a href="#cite_ref-g_1-4">1.04</a></sup> <sup><a href="#cite_ref-g_1-5">1.05</a></sup> <sup><a href="#cite_ref-g_1-6">1.06</a></sup> <sup><a href="#cite_ref-g_1-7">1.07</a></sup> <sup><a href="#cite_ref-g_1-8">1.08</a></sup> <sup><a href="#cite_ref-g_1-9">1.09</a></sup> <sup><a href="#cite_ref-g_1-10">1.10</a></sup></span> <span class="reference-text">Monsters' graphics were updated.</span></li></ol></div><table class="navbox nowraplinks mw-collapsible" data-collapsetext="hide" data-expandtext="show"><tbody><tr><th colspan="2" class="navbox-title" id="navbox-title"><div style="padding-right:0"><div class="navbar" style="float:left;text-align:left;width:6em"><div class="plainlinks noprint" style="background-color:transparent;padding:0;font-weight:normal;font-size:xx-small;white-space:nowrap"><a href="/w/Template:Bestiary" title="Template:Bestiary"><span title="View this template">v</span></a>&#160;<span style="font-size:80%">&#8226;</span>&#160;<a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="//oldschool.runescape.wiki/w/Template_talk:Bestiary"><span title="Discussion about this template">d</span></a>&#160;<span style="font-size:80%">&#8226;</span>&#160;<a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="//oldschool.runescape.wiki/w/Template:Bestiary?action=edit"><span title="You can edit this template. Please use the preview button before saving.">e</span></a></div></div><span><a href="/w/Bestiary" title="Bestiary">Bestiary</a></span></div></th></tr><tr class="navbox-group navbox-group-split"><td class="navbox-group-title-hidden" colspan="0" style="display:none"></td><td colspan="2" class="navbox-list" style="text-align:center"><ul><li><a href="/w/Bestiary/Free-to-play" title="Bestiary/Free-to-play">Free-to-play</a></li><li><a class="mw-selflink selflink">1-10</a></li><li><a href="/w/Bestiary/Levels_11_to_20" title="Bestiary/Levels 11 to 20">11-20</a></li><li><a href="/w/Bestiary/Levels_21_to_30" title="Bestiary/Levels 21 to 30">21-30</a></li><li><a href="/w/Bestiary/Levels_31_to_40" title="Bestiary/Levels 31 to 40">31-40</a></li><li><a href="/w/Bestiary/Levels_41_to_50" title="Bestiary/Levels 41 to 50">41-50</a></li><li><a href="/w/Bestiary/Levels_51_to_60" title="Bestiary/Levels 51 to 60">51-60</a></li><li><a href="/w/Bestiary/Levels_61_to_70" title="Bestiary/Levels 61 to 70">61-70</a></li><li><a href="/w/Bestiary/Levels_71_to_80" title="Bestiary/Levels 71 to 80">71-80</a></li><li><a href="/w/Bestiary/Levels_81_to_90" title="Bestiary/Levels 81 to 90">81-90</a></li><li><a href="/w/Bestiary/Levels_91_to_100" title="Bestiary/Levels 91 to 100">91-100</a></li><li><a href="/w/Bestiary/Levels_higher_than_100" title="Bestiary/Levels higher than 100">&gt;100</a></li></ul></td></tr></tbody></table><div class="hidden navbox-data" style="display:none">Navbox JSON: &#123;&#34;groups&#34;:&#91;&#123;&#34;contents&#34;:&#91;&#123;&#34;text&#34;:&#34;Free-to-play&#34;,&#34;link&#34;:&#34;Bestiary/Free-to-play&#34;&#125;,&#123;&#34;text&#34;:&#34;1-10&#34;,&#34;link&#34;:&#34;Bestiary/Levels 1 to 10&#34;&#125;,&#123;&#34;text&#34;:&#34;11-20&#34;,&#34;link&#34;:&#34;Bestiary/Levels 11 to 20&#34;&#125;,&#123;&#34;text&#34;:&#34;21-30&#34;,&#34;link&#34;:&#34;Bestiary/Levels 21 to 30&#34;&#125;,&#123;&#34;text&#34;:&#34;31-40&#34;,&#34;link&#34;:&#34;Bestiary/Levels 31 to 40&#34;&#125;,&#123;&#34;text&#34;:&#34;41-50&#34;,&#34;link&#34;:&#34;Bestiary/Levels 41 to 50&#34;&#125;,&#123;&#34;text&#34;:&#34;51-60&#34;,&#34;link&#34;:&#34;Bestiary/Levels 51 to 60&#34;&#125;,&#123;&#34;text&#34;:&#34;61-70&#34;,&#34;link&#34;:&#34;Bestiary/Levels 61 to 70&#34;&#125;,&#123;&#34;text&#34;:&#34;71-80&#34;,&#34;link&#34;:&#34;Bestiary/Levels 71 to 80&#34;&#125;,&#123;&#34;text&#34;:&#34;81-90&#34;,&#34;link&#34;:&#34;Bestiary/Levels 81 to 90&#34;&#125;,&#123;&#34;text&#34;:&#34;91-100&#34;,&#34;link&#34;:&#34;Bestiary/Levels 91 to 100&#34;&#125;,&#123;&#34;text&#34;:&#34;&#62;100&#34;,&#34;link&#34;:&#34;Bestiary/Levels higher than 100&#34;&#125;&#93;&#125;&#93;,&#34;name&#34;:&#34;Bestiary&#34;,&#34;title&#34;:&#34;&#91;&#91;Bestiary&#93;&#93;&#34;&#125;</div><!-- NewPP limit reportCached time: 20190510020916Cache expiry: 86400Dynamic content: false[SMW] In‐text annotation parser time: 0.004 secondsCPU time usage: 0.097 secondsReal time usage: 0.108 secondsPreprocessor visited node count: 175/1000000Preprocessor generated node count: 390/1000000Post‐expand include size: 8847/2097152 bytesTemplate argument size: 0/2097152 bytesHighest expansion depth: 4/40Expensive parser function count: 0/100Unstrip recursion depth: 0/20Unstrip post‐expand size: 1694/5000000 bytesLua time usage: 0.016/7.000 secondsLua memory usage: 699 KB/350 MB--><!--Transclusion expansion time report (%,ms,calls,template)100.00% 39.002 1 Template:Bestiary100.00% 39.002 1 -total 82.33% 32.112 1 Template:Navbox 13.50% 5.266 1 Template:Ctg--></div><!-- Saved in parser cache with key en_osrswiki:pcache:idhash:18182-0!canonical and timestamp 20190510020916 and revision id 8108670 --></div><div class="printfooter">Retrieved from ‘<a dir="ltr" href="https://oldschool.runescape.wiki/w/Bestiary/Levels_1_to_10?oldid=8108670">https://oldschool.runescape.wiki/w/Bestiary/Levels_1_to_10?oldid=8108670</a>’</div><div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/w/Special:Categories" title="Special:Categories">Category</a>: <ul><li><a href="/w/Category:Bestiary" title="Category:Bestiary">Bestiary</a></li></ul></div></div><div class="visualClear"></div></div></div><div id="mw-navigation"><h2>Navigation menu</h2><div id="mw-head"><div id="p-personal" role="navigation" class="" aria-labelledby="p-personal-label"><h3 id="p-personal-label">Personal tools</h3><ul><li id="pt-anonuserpage">Not logged in</li><li id="pt-anontalk"><a href="/w/Special:MyTalk" title="Discussion about edits from this IP address [n]" accesskey="n">Talk</a></li><li id="pt-anoncontribs"><a href="/w/Special:MyContributions" title="A list of edits made from this IP address [y]" accesskey="y">Contributions</a></li><li id="pt-createaccount"><a href="/w/Special:CreateAccount?returnto=Bestiary%2FLevels+1+to+10" title="You are encouraged to create an account and log in; however, it is not mandatory">Create account</a></li><li id="pt-login"><a href="/w/Special:UserLogin?returnto=Bestiary%2FLevels+1+to+10" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o">Log in</a></li></ul></div><div id="left-navigation"><div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label"><h3 id="p-namespaces-label">Namespaces</h3><ul><li id="ca-nstab-main" class="selected"><span><a href="/w/Bestiary/Levels_1_to_10" title="View the content page [c]" accesskey="c">Article</a></span></li><li id="ca-talk"><span><a href="/w/Talk:Bestiary/Levels_1_to_10" rel="discussion" title="Discussion about the content page [t]" accesskey="t">Discussion</a></span></li></ul></div><div id="p-variants" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-variants-label"><input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-variants-label"/><h3 id="p-variants-label"><span>Variants</span></h3><div class="menu"><ul></ul></div></div></div><div id="right-navigation"><div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label"><h3 id="p-views-label">Views</h3><ul><li id="ca-view" class="collapsible selected"><span><a href="/w/Bestiary/Levels_1_to_10">Read</a></span></li><li id="ca-ve-edit" class="collapsible"><span><a href="/w/Bestiary/Levels_1_to_10?veaction=edit" title="Edit this page [v]" accesskey="v">Edit</a></span></li><li id="ca-edit" class="collapsible"><span><a href="/w/Bestiary/Levels_1_to_10?action=edit" title="Edit this page [e]" accesskey="e">Edit source</a></span></li><li id="ca-history" class="collapsible"><span><a href="/w/Bestiary/Levels_1_to_10?action=history" title="Past revisions of this page [h]" accesskey="h">History</a></span></li></ul></div><div id="p-cactions" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-cactions-label"><input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-cactions-label"/><h3 id="p-cactions-label"><span>More</span></h3><div class="menu"><ul></ul></div></div><div id="p-search" role="search"><h3><label for="searchInput">Search</label></h3><form action="/" id="searchform"><div id="simpleSearch"><input type="search" name="search" placeholder="Search Old School RuneScape Wiki" title="Search the wiki [f]" accesskey="f" id="searchInput"/><input type="hidden" value="Special:Search" name="title"/><input type="submit" name="fulltext" value="Search" title="Search pages for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton"/><input type="submit" name="go" value="Go" title="Go to a page with this exact name if it exists" id="searchButton" class="searchButton"/></div></form></div></div></div><div id="mw-panel"><div id="p-logo" role="banner"><a class="mw-wiki-logo" href="/" title="Visit the main page"></a></div><div class="portal" role="navigation" id="p-Navigation" aria-labelledby="p-Navigation-label"><h3 id="p-Navigation-label">Navigation</h3><div class="body"><ul><li id="n-Main-page"><a href="/">Main page</a></li><li id="n-About-us"><a href="/w/RuneScape:About">About us</a></li><li id="n-Recent-changes"><a href="/w/Special:RecentChanges">Recent changes</a></li><li id="n-New-files"><a href="/w/Special:NewFiles">New files</a></li><li id="n-Random-page"><a href="/w/Special:Random/main">Random page</a></li><li id="n-Contact-us"><a href="/w/RuneScape:Contact_us">Contact us</a></li><li id="n-Help"><a href="/w/RuneScape:User_help">Help</a></li></ul></div></div><div class="portal" role="navigation" id="p-Guides" aria-labelledby="p-Guides-label"><h3 id="p-Guides-label">Guides</h3><div class="body"><ul><li id="n-Recent-updates"><a href="/w/2019">Recent updates</a></li><li id="n-List-of-quests"><a href="/w/List_of_quests">List of quests</a></li><li id="n-Achievement-Diaries"><a href="/w/Achievement_Diary">Achievement Diaries</a></li><li id="n-Skill-training"><a href="/w/Skill_training_guides">Skill training</a></li><li id="n-Money-making"><a href="/w/Money_making_guide">Money making</a></li><li id="n-Treasure-Trails"><a href="/w/Treasure_Trails/Guide">Treasure Trails</a></li></ul></div></div><div class="portal" role="navigation" id="p-Community" aria-labelledby="p-Community-label"><h3 id="p-Community-label">Community</h3><div class="body"><ul><li id="n-User-help"><a href="/w/RuneScape:User_help">User help</a></li><li id="n-Discussions"><a href="/w/Forum:RuneCaf%C3%A9">Discussions</a></li><li id="n-Frequently-asked-questions"><a href="/w/RuneScape:Frequently_asked_questions">Frequently asked questions</a></li><li id="n-Discord-server"><a href="/w/RuneScape:Discord">Discord server</a></li></ul></div></div><div class="portal" role="navigation" id="p-More_RuneScape" aria-labelledby="p-More_RuneScape-label"><h3 id="p-More_RuneScape-label">More RuneScape</h3><div class="body"><ul><li id="n-RuneScape-Wiki"><a href="//runescape.wiki/w/RuneScape_Wiki">RuneScape Wiki</a></li><li id="n-RSC-Wiki"><a href="https://classic.runescape.wiki/RuneScape_Classic_Wiki">RSC Wiki</a></li><li id="n-OSRS-Website"><a href="https://oldschool.runescape.com/" rel="nofollow" target="_blank">OSRS Website</a></li><li id="n-RuneScape-Forums"><a href="http://services.runescape.com/m=forum/forums.ws#group63" rel="nofollow" target="_blank">RuneScape Forums</a></li></ul></div></div><div class="portal" role="navigation" id="p-tb" aria-labelledby="p-tb-label"><h3 id="p-tb-label">Tools</h3><div class="body"><ul><li id="t-whatlinkshere"><a href="/w/Special:WhatLinksHere/Bestiary/Levels_1_to_10" title="A list of all wiki pages that link here [j]" accesskey="j">What links here</a></li><li id="t-recentchangeslinked"><a href="/w/Special:RecentChangesLinked/Bestiary/Levels_1_to_10" rel="nofollow" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li><li id="t-specialpages"><a href="/w/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li><li id="t-print"><a href="/w/Bestiary/Levels_1_to_10?printable=yes" rel="alternate" title="Printable version of this page [p]" accesskey="p">Printable version</a></li><li id="t-permalink"><a href="/w/Bestiary/Levels_1_to_10?oldid=8108670" title="Permanent link to this revision of the page">Permanent link</a></li><li id="t-info"><a href="/w/Bestiary/Levels_1_to_10?action=info" title="More information about this page">Page information</a></li><li id="t-smwbrowselink"><a href="/w/Special:Browse/:Bestiary-2FLevels-5F1-5Fto-5F10" rel="search">Browse properties</a></li></ul></div></div></div></div><div id="footer" role="contentinfo"><ul id="footer-info"><li id="footer-info-lastmod"> This page was last modified on 5 December 2018, at 03:29.</li><li id="footer-info-copyright">Content on this site is licensed under <a class="external" rel="nofollow" href="https://creativecommons.org/licenses/by-nc-sa/3.0/">CC BY-NC-SA 3.0</a>; <a href="https://meta.weirdgloop.org/w/Project:Copyrights">additional terms apply</a>.<br/><i>RuneScape</i> and <i>RuneScape Old School</i> are the trademarks of <a href="http://jagex.com">Jagex Limited</a> and are used with the permission of Jagex.</li></ul><ul id="footer-places"><li id="footer-places-privacy"><a href="//weirdgloop.org/privacy" class="extiw" title="wg:privacy">Privacy policy</a></li><li id="footer-places-about"><a href="/w/RuneScape:About" title="RuneScape:About">About Old School RuneScape Wiki</a></li><li id="footer-places-disclaimer"><a href="/w/RuneScape:General_disclaimer" title="RuneScape:General disclaimer">Disclaimers</a></li><li id="footer-places-tou"><a href="https://weirdgloop.org/terms">Terms of Use</a></li><li id="footer-places-contact"><a href="/w/Special:Contact">Contact Weird Gloop</a></li><li id="footer-places-mobileview"><a href="//oldschool.runescape.wiki/w/Bestiary/Levels_1_to_10?mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Mobile view</a></li></ul><ul id="footer-icons" class="noprint"><li id="footer-copyrightico"><a href="https://creativecommons.org/licenses/by-nc-sa/3.0/" target="_blank"><img src="https://weirdgloop.org/images/mw/cc-by-nc-sa.png" alt="CC BY-NC-SA 3.0" srcset="https://weirdgloop.org/images/mw/cc-by-nc-sa@2x.png 2x" width="88" height="31"/></a></li><li id="footer-poweredbyico"><a href="https://weirdgloop.org" target="_blank"><img src="https://weirdgloop.org/images/mw/weirdgloop.png" alt="A Weird Gloop wiki" srcset="https://weirdgloop.org/images/mw/weirdgloop@2x.png 2x" height="31" width="88"/></a></li></ul><div style="clear: both;"></div></div><script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"smw":{"limitreport-intext-parsertime":0.004},"limitreport":{"cputime":"0.097","walltime":"0.108","ppvisitednodes":{"value":175,"limit":1000000},"ppgeneratednodes":{"value":390,"limit":1000000},"postexpandincludesize":{"value":8847,"limit":2097152},"templateargumentsize":{"value":0,"limit":2097152},"expansiondepth":{"value":4,"limit":40},"expensivefunctioncount":{"value":0,"limit":100},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":1694,"limit":5000000},"timingprofile":["100.00% 39.002 1 Template:Bestiary","100.00% 39.002 1 -total"," 82.33% 32.112 1 Template:Navbox"," 13.50% 5.266 1 Template:Ctg"]},"scribunto":{"limitreport-timeusage":{"value":"0.016","limit":"7.000"},"limitreport-memusage":{"value":716052,"limit":367001600}},"cachereport":{"timestamp":"20190510020916","ttl":86400,"transientcontent":false}}});});</script><script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":82});});</script></body></html>
"""


def fetch():
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find(class_="mw-content-ltr")

    links = []

    for n in body.find_all('li'):
        if n.find('a'):
            slug = n.find('a').get('href', '')
            if "#" not in slug and "Bestiary" not in slug and slug:
                links.append("https://oldschool.runescape.wiki" + slug)

    return links
