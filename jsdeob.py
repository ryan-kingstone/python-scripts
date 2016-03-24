# purpose 	aid the deobfuscation process of the min.js from the rainingchan repository.

import os
import sys
import re
import time

#initialize the array of replacement strings
replaces = ["use strict", "init_app", "Using MINIFY.\x0D\x0ATo play, open Google Chrome and go to the url \"localhost:3000\".", "Cant use NODEJITSU and MINIFY", "argv", "d", "doNotStartServer", "alias", "o", "onlineDb", "i", "integrityTest", "yargs", "deleteDb", "path", "express", "Server", "http", "socket.io", "listen", "PORT", "env", "client", "../client", "resolve", "static", "use", "json", "body-parser", "urlencoded", "compression", "init_ModuleManager", "./ModuleManager", "setInitDbHttp", "./InitDb", "Send info to connect to the database.", "Initializing server...", "initDb", "init", "./Db_private", "account", "require", "isEmailActive", "./Email", "/tutorial/:page", "page", "params", "tutorial/", "tutorial", "render", "get", "/wiki/:page", "wiki/", "wiki", "/patchNotes", "patchNotes", "/QuestCreator/API", "QuestCreator/API", "QuestCreator", "/QuestCreator/tutorial", "QuestCreator/tutorial", "/QuestCreator/feedback", "QuestCreator/feedback", "/QuestCreator/localdb", "QuestCreator/localdb", "/QuestCreator", "/contribution", "contribution", "/game", "game", "isReady", "/", "index", "getPlayerCount", "getCompetitionHomePageContent", "getHighscoreHomePageContent", "arrayToTable", "locals", "view engine", "html", "set", "views", ".html", "__express", "ejs", "engine", "VersionControl", "./VersionControl", "<table>", "<thead><tr>", "length", "<th>", "</th>", "</thead>", "<tbody>", "<tr>", "<td>", "</td>", "</tr>", "</tbody>", "number", "Episode ", "youtube", "", "pastebin", "http://www.youtube.com/embed/", "http://pastebin.com/", "dpIADPTu820", "ajrr7Drq", "DeuQ9RqJ", "XsM0tSFaqnw", "TA2zpf3p", "zH9z7bs15qk", "bGHF49Cm", "lmOtxsrEwaI", "sg8sQAK3", "ffnmy-BGSwc", "TdVRjUPs", "gy_0Dm-eeaI", "YynB2Fcq", "Ml2nX_nezZY", "nE9kpgZQ", "TnhlOmb2Gxw", "2JV14HBH", "WimNnvbuXJc", "bsxxhLJY", "7gdtg-KiXEQ", "6mBSK7XP", "VKCEggooLFc", "9YMpXMba", "F2Dc-JlwgN4", "35UyaUBb", "WfL4LNUL3R0", "zLM8QhTm", "EBKcnNGwFGY", "HNdRreJs", "HxyGXumEWB0", "XfYCJ3k2", "XgK4YaMqQFg", "CzNtUr1B", "connection", "signIn", "loginErrorMessage", "getAttr", "emit", "on", "sockets", "busy", "/ERROR", "LOG", "send", "./../client/pokemon/POKEMON_server", "./../client/zelda/ZELDA_server", "./../client/rs/RS_server", "status", "Cant find that file, sorry!", "statusCode", "blocked", "I\'m busy right now, sorry.", "require2", "require3", "require4", "loadAPI", "requireModuleList", "TreeDependency", "./TreeDependency", "getPath", "client-", "./client/js/", "./../client/js/", "shared", "./client/js/shared/", "./../client/js/shared/", "server", "./", "./../", "private", "./min", "add", "Tk", "ERROR", "CST", "SpriteFilter", "Song", "Socket_client", "Sign_client", "Sfx", "Receive", "Pref", "Performance_client", "Message_receive", "Message_client", "MapModel_client", "Input_client", "Img", "Game", "Draw", "Dialog_topRight", "Dialog_topLeft", "Dialog_stat", "Dialog_setting", "Dialog_reputation", "Dialog_questList", "Dialog_quest", "Dialog_misc", "Dialog_itemList", "Dialog_highscore", "Dialog_friend", "Dialog_equip", "Dialog_contribution", "Dialog_bottomRight", "Dialog_bottomLeft", "Dialog_binding", "Dialog_achievement", "Dialog_ability", "Dialog", "ClientPrediction", "Anim_client", "Account", "Metrics", "Weather", "Send", "SkillPlotModel", "Highscore", "QuestVar", "Quest_status", "Preset", "Challenge", "Quest", "Performance", "Party", "OfflineAction", "Message_server", "Material", "MapGraph", "MapModel", "Maps", "Input", "Equip", "Dialogue", "Debug", "Cycle", "CraftBoost", "Competition", "Combat", "Boss", "ActorGroup", "ActiveList", "Ability", "Anim", "LightingEffect", "Achievement", "IconModel", "ClientError", "Strike", "Stat", "SpriteModel", "Sprite", "ReputationConverter", "ReputationGrid", "OptionList", "Message", "Main_achievement", "Main_screenEffect", "Main_contribution", "Main_dailyTask", "Main_party", "Main_temp", "Main_social", "Main_question", "Main_quest_status", "Main_quest", "Main_reputation", "Main_loop", "Main_itemlist", "Main_dialogue", "Main_chrono", "Main_change", "Main", "ItemModel", "ItemList", "Drop", "QueryDb", "Command", "Combat_shared", "Collision", "Button", "Bullet", "Boost", "BISON", "AttackModel", "Attack", "AnimModel", "Actor_questMarker", "Actor_teleport", "Actor_status", "Actor_skill", "Actor_move", "Actor_loop", "Actor_interaction", "Actor_equip", "Actor_draw", "Actor_death", "Actor_combat", "Actor_change", "Actor_boost", "Actor_ai", "Actor_ability", "ActorModel", "Actor", "IntegrityTest", "SocialMedia", "Debug_server", "Reddit", "Socket", "Sign", "Save", "apply", "newQuest", "./Quest_API", "directory", "localhost:27017/test", "clientError", "socialMedia", "pingData", "report", "player", "contributionHistory", "offlineAction", "main", "equip", "competition", "questRating", "highscore", "questVar", "mainQuest", "mongojs", "public", "publictest", "kahana.mongohq.com", "10086", "sam", "mongodb://", "username", ":", "password", "@", "port", "db", "databaseURI", "connectionString", "B", "close", "options", "connect", "LOCAL DB", "remove", "DELETED EVERYTHING IN DATABASE!", "./Db_maintenance", "isArray", "$contains", "table dont exist", "Part", "err", "aggregate", "insert", "upsert", "update", "findOne", "find", "_id", "function", "Q", "quest id needs to start with Q", "version", "id", "quest", "getAPItemplate", "addPrefix", "adding prefix to nothing", "format", "-", "skillPlot", "skillPlotAllowed", "not allowed skillplot", "dialogue", "normal", "teleport", "deathEvent", "viewedIf", "Qsystem-", "no npc with that model", "isInMap", "map", "monster spawning in wrong map", "object", "x", "y", "map model dont exist", "addon", "no addon for that quest", "spot", "deepClone", "spot not found ", "key not in map", "isPlayer", "getParty", "forEach", "event", "no event with id", "questStart", "openDialog", "setAttr", "one", "getItemAmount", "haveItem", "removeItem", "addItem", "getSpot", "simulatePush", "healParty", "healActor", "respawnParty", "respawnPlayer", "setSpriteFilter", "setHp", "addHp", "rechargeAbility", "killActor", "killParty", "actorExists", "removeBoost", "addBoost", "setSprite", "enableMove", "enablePvp", "enableCombat", "enableAttack", "enableReputation", "addEquip", "hasAbility", "addAbility", "removePreset", "hasPreset", "usePreset", "addAnimOnTop", "addAnim", "list", "spawnActorGroup", "spawnActorOnTop", "spawnActor", "forEachActor", "setTag", "getTag", "hasTag", "getRandomNpc", "getRandomPlayer", "moveActor", "getPosition", "getDistance", "isInQuestMap", "isAtSpot", "isAtPosition", "removeAllQuestMarker", "removeQuestMarker", "addQuestMarker", "endPath", "followPath", "setRespawn", "teleportTown", "force", "restoreHUD", "setHUD", "startWeatherRain", "removeScreenEffect", "shakeScreen", "addTorchEffect", "addFadeout", "setInterval", "setTimeout", "removeChrono", "stopChrono", "startChrono", "isInDialogue", "endDialogue", "button", "displayPermPopup", "closePermPopup", "startDialogue", "displayQuestion", "displayPopup", "input", "message", "isChallengeActive", "getPartySize", "isOnline", "hasQuestActive", "testQuestActive", "completeQuest", "failQuest", "startQuest", "frameToChrono", "callEvent", "getEvent", "b", "m", "newQuest_new", "newQuest_map", "newQuest_boss", "./Quest_API_new", "./Quest_API_map", "./Quest_API_boss", "event undefined", "push", "getKeyList", "abandonQuest", "You have failed the quest ", "name", ".", "undefined", "random", "p", "randomId", "questActive", "alwaysActive", "getViaMain", "getSize", "inMain", "trying to access not inMain var", "you need to declare the variable in s.newVariable first", "updateQuestHint", "_challenge", "<span style=\"color:", "\">", "</span>", "[$", "]", "addPopup", "question", "start", "permPopup", "aboveInventory", "<button style=\"", "\" title=\"", "\" onclick=\"exports.Command.execute(\'questButton\',[\'", "\']);\">", "</button>", "end", "chrono", "stop", "time NaN", "fadeout", "ScreenEffect", "addScreenEffect", "torch", "shake", "removeFadeout", "removeTorchEffect", "stopShakingScreen", "rain", "hudState", "invalid hud name", "admin", "minimap", "hp", "mana", "abilityBar", "curseClient", "inventory", "cant change hudState of", "NORMAL", "invisible", "INVISIBLE", "flashing", "invalid hud value", "FLASHING", "Date", "P", "party", "solo", "@@", "cant call s.teleport.one and overwrite new map at same time.", "fromQuest", "isActive", "town", "no spot", "combat", "abs", "getDistancePtPt", "moveBy", "tag", "actor is not in map", "trying to spawn monster while player is not in map", "v", "randomML", "Spot", "trying to spawn anim while player is not in map", "anim", "newAbility", "true", "Target", "create", "addPreset", "preset", "ability", "no ability", "swapAbility", "getAbility", "changeEquip", "updateBoost", "reputation", "BOOST_NAME", "permBoost", "noAbility", "removeAll", "boost", "pvpEnabled", "setFlag", "damagedIf", "damageIf", "npc", "move", "changeSprite", "sizeMod", "*", "***", "Perm", "removeById", "kill", "type", "changeHp", "red", "green", "blue", "allBlack", "dodge", "invalid filter", "dead", "onCommandRespawn", "hpMax", "manaMax", "down", "up", "left", "right", "invalid direction", "pushable", "initPushable", "not pushable", "not allowed to change player attr", "not allowed to set this attr", "not allowed to get this attr", "getReputationUsedPt", "getLevel", "permanently", "iconToText", "playSong", "playSfx", "setPermData", "getPermData", "getQuestPermData", "setQuestPermData", "<img src=\"../img/ui/icon/", ".png\" width=\"20px\">", "invalid icon", "not admin", "invalid spot", "need to be admin", "getUsedPt", "boss", "getRandomTargetAngle", "getRandomTarget", "attackOff", "getSummonCount", "useAbility", "no ability,name", "getSummon", "_", "cant modify internal values", "variable", "act dont exist", "NaN", "_noattack", "return", "spawnBlock", "spot dont exist", "addToMap", "NPC_RESPAWN", "List", "spike", "sprite", "newNpc", "width", "height", "max", "floor", "block-spike", "x1", "block", "size", "block-spike1x", "block-spike1x1", "testInterval", "addTeleport", "addDialogue", "translateSpot", "spawnBank", "spawnSkillPlot", "spawnSignpost", "spawnLoot", "spawnWaypoint", "spawnTeleporter", "spawnToggle", "toggle-", "On", "toggle", "Off", "box", "interactionMaxRange", "This switch is already active.", "teleport-", "zone", "string", "angle", "waypoint-grave", "waypoint", "loot-", "loot", "chest", "signpost", "text not a func or string", "system-sign", "downModel", "SkillPlot", "num", "_skillPlot", "model", "system-bank", "addBankSpot", "no actor has tag", "this actor needs a dialogue to start things off.", "this actor needs a teleport to start things off.", "testPtRect", "actor", "getActorInMap", "getNpcInMap", "invalid actorType", "getPlayerInMap", "splice", "Qsystem", "newHighscore", "newChallenge", "option", "newItem", "newEvent", "newVariable", "Model", "cant create new stuff at this point", "item", "Option", "challenge", "attack", "attackMagic-fireball", "Deal damage.", "heal", "heal-plus", "Heal", "Replenish resources.", "boostRed", "blessing-spike", "Dodge", "Makes you invincible for a bit.", "summon", "summon-wolf", "Summon", "Standard healing.", "boostPink", "Blessing", "Boost a stat.", "idle", "invalid template", "Event", "Custom Event", "exports", "compileSpotList", "newPath", "spotChain", "spotList", "newBoss", "phase", "newDialogue", "node", "newMapAddon", "newMap", "immune", "side", "onclick", "targetSetting", "abilityAi", "statusResist", "mastery", "moveRange", "maxSpd", "newPreset", "newEquip", "newBoost", "hitEvent", "spriteFilter", "spd", "initPosition", "onHitHeal", "curse", "parabole", "sin", "boomerang", "onMove", "pierce", "onHit", "dmg", "strike", "warning, strike but no initPosition", "param", "no ability template", "melee", "Dmg", "range", "magic", "fire", "cold", "lightning", "invalid element", "Base", "onDamagePhase", "OnHit", "Pierce", "OnMove", "Status", "Boomerang", "Sin", "Parabole", "Curse", "OnHitHeal", "InitPosition", "BULLETSPD", "event not found", "Param", "piece", "NPCSPD", "MoveRange", "element", "Mastery", "part", "StatusResist", "AbilityAi", "invalid distanceInfo", "no ability with this id", "Block", "Pushable", "TargetSetting", "param must be array", "Click", "no func", "template", "MapAddon", "Node", "startingPhase", "$isEmpty", "Phase", "Variable", "Path", "raw", "showInTab", "s", "_score", "Quest Score", "Cumulative Quest Score (Increase every time you complete the quest.)", "descending", "_rewardScore", "If popup text doesn\'t disappear, press Esc.", "Press tab to reply to last player who PMed you.", "Press Esc to remove current input in chat and close windows.", "If someone is bothering you, add him to your mute list by right-clicking his name in the chat.", "This game started off as a Flash game.", "Coding for this game was done exclusively with Notepad++.", "There are 3 types of map instances: public, party and solo.", "Using an ability that matches the weapon elemental type will increase damage by 50%.", "You can only harvest Skill Plots once (ex: trees). To harvest it again, you need to complete the related quest. This is to prevent grinding and botters.", "Monsters give exp and items upon killing. However, the loot has diminishing returns. (The more you kill, the less likely you will get loot.) Completing the quest related to the enemies will reset the diminishing returns.", "Levelling your combat stats will increase damage dealt and your defence. You will also be able to use better weapons and armors.", "If you no longer need an equip, you can salvage it into useful materials.", "When looting an equip, most of its boosts will be locked. Use materials to upgrade the equip and make it more powerful.", "In the quest tab, you can shift-left click to start/abandon quests quickly.", "Levelling-up grants a Reputation point that can be used to boost a stat of your choice via the Reputation Grid.", "Shift-Leck-Click an item in inventory to show it in chat.", "You need to beat a quest at least once before activating a challenge.", "Every Melee Ability has a default 5% chance to bleed. Bleed deals damage over time.", "Every Range Ability has a default 5% chance to knockback, pushing the enemy away from you.", "Every Magic Ability has a default 5% chance to drain mana and replenish yours.", "Every Fire Ability has a default 5% chance to burn. Burning deals damage over time related to the remaining life.", "Every Cold Ability has a default 5% chance to chill which reduces movement and attack speed.", "Every Lightning Ability has a default 5% chance to stun. Stunning stops the targets and reduces its ability charges, delaying its next attack.", "To send a private message, type @[player name],[message]. Ex: @bob532563,hey ", "Stat boosts can come from your equips or the reputation grid.", "There is 2 types of cooldowns. The \'global\' cooldown prevents you from using any another ability while the \'own\' cooldown prevents you from using the same ability again.", "The most powerful abilities require mana. If you don\'t have enough mana, you can\'t use them.", "Some abilities trigger other attack while moving, hitting a target, or reaching damage phase.", "loadMainQuest", "in", "getSignInPack", "loadPlayer", "loadQuestVar", "loadMain", "addToGame", "load", "onError", "off", "response", "<font color=\"", "</font>", "email", "signUp", "Invalid Email.", "user", "isBannedName", "Illegal characters in username.", "isAdmin", "Too short username.", "Too long username.", "getMinPasswordLength", "Too short password.", "getMaxPasswordLength", "Too long password.", "This username is already taken.", "encryptString", "onSignUp", "slice", "toString", "salt", "geoLocation", "New Account Created.<br>You can now Sign In.", "sendActivationKey", "insertInDb", "beingRemoved", "onSignOff", "data", "invList", "bankList", "getEquip", "addPingDataToDb", "signOff", "<span>You have been disconnected.</span><br>", "no socket", "key", "disconnect", "removeUsernameToKey", "removeFromList", "no act with key ", "passwordAcceptedSigninIn", "The server is trying to log you in.<br>Wait 30 seconds and refresh the page if nothing is happening.", "banned", "This account is banned.", "Wrong Password or Username.", "getViaUserName", "online", "This account was online.<br>We just logged it off.<br>Try connecting again.", "setOfflineInDb", "Loading account...", "onSignIn", "addToList", "getRespawnSpot", "uncompressDb", "$keys", "concat", "checkIntegrity", "fetchList", "fetch", "lastSignIn", "$random", "getHomePageContent", "verifyIntegrity", "urlDownloadGameEngine", "urlDownloadQuestCreator", "urlDownloadUpdater", "LIST", "toEval", "NODEJS_MESSAGE", "UPDATER_MESSAGE", "UPDATER", "QUEST_CREATOR", "GAME_ENGINE", "1.4.0", "1.2.0", "1.0.0", "http://download1647.mediafire.com/gdb2gi85liog/256fmcenu3hykcw/RainingChainUpdater.exe", "http://download1502.mediafire.com/fh2e6lc2wwxg/czxzamsb31arx5r/QuestCreator.zip", "http://github.com/RainingChain/rainingchain/archive/master.zip", "/checkUpdate", "/checkUpdate?", "replace", "url", "parse", "SD", "Your game engine is outdated.<br>Run RainingChainUpdater.exe to update it.", "rainingchain", "/getDevMessage", "The game engine and Quest Creator you are using are no longer supported.<br>Download the new Quest Creator that handles Auto Updates at <a style=\"color:blue\" target=\"_blank\" href=\"http://www.rainingchain.com/contribution/\">", "http://rainingchain.com/checkUpdate?", "SUBDOMAIN", "process", "stringify", "nodejsMessage", "request", "MIN", "HOUR", "Error with request \"", "\". Reload the page.", "now", "emitCount", "globalTimer", "limitPerMin", "emitLast", "minInterval", "func", "click", "timeOfLastEmit", "DOWNLOAD", "bandwidth", "ping", "uploadMod", "queryDb", "command", "sendChat", "clientReady", "DB", "getTimePlayedSinceLastCall", "loop", "FRAME_COUNT", "addPingData", "pingDataCount", "pingSum", "round", "shutdown", "Disconnected due to inactivity.", "connectionStartTime", "Disconnected due because max session time reached.", "toRemove", "lastCallForTimePlayed", "receiveError", "socketManagement", "handClickServerSide", "respond", "receive", "Verifying password...", "Creating account...", "crypto", "addUsernameToKey", "getKeyViaUsername", "USERNAME_TO_ID", "TIMELIMIT_PERWEEK", "prop not in constructor", "ALL", "<div class=\"container\"><h3>Email Confirmation</h3><p>", "</p></div>", "/confirmEmail", "confirmKey", "query", "emailActivated", "confirmEmail", "Your account was already activated.<br><br>Play now at <a style=\"color:cyan\" href=\"/\">www.RainingChain.com</a>", "Your account has been successfully activated.<br><br>Play now at <a style=\"color:cyan\" href=\"/\">www.RainingChain.com</a>", "No email is associated with the activation key \"", "\".", "getKeyViaName", "emailActivationKey", "Wrong key.", "You successfully activated your account.", "requestResetPassword", "NO_ACCOUNT", "No account found with this username.", "NO_EMAIL", "Your account has no email linked to it. The only way for you to recover it is to remember your password.", "BAD_EMAIL", "Email doesn\'t match username.<br>", "A Reset Password Key has been sent to you by email. You will need use it to reset your password.", "resetPassword", "resetPasswordKey", "no account", "no email", "This account has no email.", "no resetPasswordKey", "No request was made to reset this password.", "bad resetPasswordKey", "Wrong Reset Password Key. The key was sent to you via email.", "old resetPasswordKey", "Your Reset Password Key has expired, please send a new request to reset the password.", "Password reset. A new randomly-generated password has been sent to you via email.<br> Upon signing in, you will be asked to change it.", "changeEmail", "Wrong current password.", "emailChangeRequest", "DAY", "You will be able to change your email in ", "r", " hours.", "Email changed.", "You successfully requested a email change. You will be able to change the email in 3 days.", "Invalid email.", "abortChangeEmail", "You successfully aborted the change of your email.", "changePassword", "oldPassword", "newPassword", "Password too short.", "Password too long.", "Password changed.", "You need to be logged in to perform that action.", "Problem with your query: ", "stack", "usernameExists", "resetTimePlayedThisWeek", "unban", "ban", "sendRandomlyGeneratedPasswordMessage", "sendEmailChangeRequestMessage", "sendTimePlayedMessage", "randomString", "getSalt", "SUCCESS", "BAD_RESETPASSWORDKEY", "OLD_RESETPASSWORDKEY", "NO_RESETPASSWORDKEY", "bad email", "Welcome to Raining Chain! This is your activation key for your account ", ": ", "Raining Chain: Activation Key", "binary", "base64", "pbkdf2", "randomBytes", "Raining Chain Reset Password Key", "A request to reset the password for the account ", " has been made. If you have not requested this, ignore this message.\x0D\x0AHere is your Reset Password Key: ", "resetPasswordTime", "day", "resetPasswordSalt", "Raining Chain Password Reset", "The password for the account ", " has been reset to: ", " .", "A request to change your email has been made. You can abort the change by going in the account management window via the Pref Tab.", "You can now change your email.", "randomlyGeneratedPassword", "Change your password via the Pref Tab.", "$ALL$", "You have been banned. ", "no player with this name", "updateBannedName", "mute", "clearList", "reset", "getPlayerInfo", "INFO", "LEVEL", "log", "DATA", "display", "disconnectAll", "ADMIN_RC", "Server is currently down.<br>Come back later.", "rc", "Server ready", "ready", "Admin disconnected every player.", "adminList", ", ", "toGMTString", "time", "\x0A  ---  ", "getHomePageRank", "getAct", "category", "lookingFor", "comment", "updatePlayerOnline", "onServerReset", " Server crash #", "COUNT", "\x0A", "Saved player data: ", "sendCrashReport", "SERVER HAS BEEN RESET", "Server Reset: ", "Warning, ERROR display is false", "About to reset the server...", "The server needs to be updated. It will reset in ", " seconds.", "You have been muted.", "addMessage", "muted", "social", "You are no longer muted.", "getOwnPropertyNames", "bannedName", "prototype", "no player?", "compressDb", "compress result is null", "no main?", "saveAllScore", "nothing from QuestVar getViaMain", "_started"]

l = []

def replace_word(infile, old_word, new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word, new_word)
    f2.write(m)

def perform():
    start = time.time()

    for i in xrange(len(replaces)):
        replace_word("../script.js", '_$_c7c7[' + str(i) + ']', "\"" + replaces[i] + "\"")
        print(str(i) + " " + replaces[i])

    end = time.time()
    elapsed = end - start
    print str(elapsed) + "s elapsed newfile..."

perform()