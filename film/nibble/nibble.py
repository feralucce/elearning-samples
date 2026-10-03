"""Nibble (MFA thesis short, University of New Orleans): the production paperwork as data.

Transcribed from the thesis appendix: preproduction schedule (Apr-Aug 2024), the one-strip
shooting schedule, the EP Budgeting (Movie Magic) budget, and the thesis reflection.
Personal details are removed on purpose: no address, phone or personal names; roles only.
"""

TITLE = "Nibble"
SUMMARY = ("A horror-comedy short about a pet rock that eats everyone in the house. Written, directed, shot, "
           "edited and sound-designed by Feralucce Savage as an MFA thesis film. Shot in August 2024, delivered October 2024.")

# ------------------------------------------------------------ preproduction schedule (as written, by week)
PREP = [
    ("Apr 17", "Approval", ["Submit prospectus to thesis committee"]),
    ("Apr 24", "Approval", ["Revise prospectus from committee feedback", "Set up the project drive"]),
    ("May 1", "Approval", ["Confirm prospectus with graduate committee", "Create lookbook", "Share script with potential producers and department heads"]),
    ("May 6", "Team and budget", ["Talk to potential composers", "Meet the producer team and delegate tasks"]),
    ("May 13", "Design and build", ["Research effects: blood for the shower scene, slime, waterproofing papier-mâché", "Begin location search"]),
    ("May 20", "Team and budget", ["First draft of the budget"]),
    ("May 27", "Team and budget", ["Finalise the budget"]),
    ("Jun 3", "Team and budget", ["Lock department heads", "Begin making breakaway plates"]),
    ("Jun 10", "Design and build", ["Start wardrobe and costume design", "Meet producer", "Meet production designer"]),
    ("Jun 17", "Design and build", ["Begin shot list and storyboards", "Buy googly eyes for each size of the pet rock", "Location scouting", "Post the casting notice"]),
    ("Jun 24", "Casting", ["Begin the boulder build", "Finalise shot list and storyboards", "Auditions"]),
    ("Jul 1", "Design and build", ["Finalise production design", "Finalise and 3D-scan the boulder build", "Model the pet rock for 3D printing"]),
    ("Jul 8", "Casting", ["Callbacks", "Print the pet rock in each size", "Finalise prop, wardrobe and set dressing lists", "Prepay the location", "Department head meeting"]),
    ("Jul 15", "Schedule", ["Final script pass", "Review the casting shortlist", "Shooting schedule with the 1st AD", "Performance notes with the 2nd AD"]),
    ("Jul 22", "Schedule", ["Lock actors and get sizes", "Finalise the shooting schedule", "Lock final crew"]),
    ("Jul 29", "Final prep", ["Effects test: find the best blood for the shower scene", "Buy breakaway plates, props and wardrobe", "Gear build-out and shakedown", "Production meeting"]),
    ("Aug 5", "Final prep", ["Table read and rehearsal", "Wardrobe fittings and ageing", "Make-up test", "Finalise catering"]),
    ("Aug 12", "Final prep", ["Tech scout", "Buy media storage", "Final rehearsals", "Send prep email with call times and plan", "Final production meeting"]),
    ("Aug 23", "Shoot", ["Shoot weekend 1: call sheet, set dressing, production, transcode, dailies, paperwork check"]),
    ("Aug 30", "Shoot", ["Shoot weekend 2: call sheet, production, transcode, dailies, thank-you emails"]),
]
PHASES = ["Approval", "Team and budget", "Design and build", "Casting", "Schedule", "Final prep", "Shoot"]

# ------------------------------------------------------------ cast legend (roles only)
CAST = {1: "Dani", 2: "Nell", 3: "Crusher (dog)", 4: "Suzie, the girl scout (child actor)", 5: "Nibbles (the rock)",
        6: "Announcer", 7: "Bernie", 8: "Jeanine", 9: "Doctor Compton", 10: "Crossfade element (as listed on the board)"}

# ------------------------------------------------------------ the one-strip schedule, in shooting order
# (scene, set, I/E, time of day as written or "", eighths, cast, note)
def e(whole, eighths=0):
    return whole * 8 + eighths


DAYS = [
    ("Thu Aug 22", "Playback day", "4:00 p.m.", [
        (46, "Playback: the commercial", "", "", e(0, 3), [6], ""),
        (47, "Playback: Bernie Baxter's haunted TV studio", "", "", e(0, 4), [7], ""),
        (48, "Playback: the science lab", "", "", e(1, 5), [8, 9],
         "The playback on the TV is the first scene we are shooting - it is the last scene in the script."),
    ]),
    ("Fri Aug 23", "Nell day", "7:00 a.m.", [
        (12, "Dani's house", "EXT", "Morning", e(0, 2), [2], ""),
        (14, "Dani's house", "EXT", "", e(0, 1), [2], ""),
        (16, "Dani's house", "EXT", "", e(0, 2), [2], ""),
        (26, "Dani's house", "EXT", "Evening", e(0, 1), [], ""),
        (13, "Dani's house", "INT", "", e(0, 1), [2, 5], ""),
        (15, "Dani's house", "INT", "", e(0, 1), [2, 5], ""),
        (9, "Dani's kitchen", "INT", "", e(1, 5), [2, 5, 8, 9], ""),
        (27, "Dani's bathroom", "INT", "", e(0, 2), [2], ""),
        (28, "The hallway outside the bathroom", "INT", "", e(0, 2), [5], ""),
        (29, "Dani's bathroom: the shower", "INT", "", e(0, 5), [2, 5], ""),
    ]),
    ("Sat Aug 24", "Suzie day", "7:00 a.m.", [
        (7, "Dani's kitchen: the dog bowls", "INT", "", e(0, 3), [3, 5],
         "Animal Actor - Most likely the hardest scene of the day - scheduling it first to make the day easier."),
        (8, "Dani's house", "EXT", "", e(0, 2), [3], ""),
        (17, "Dani's house: the doorbell", "EXT", "", e(0, 1), [4], ""),
        (19, "Dani's house: Suzie at the door", "EXT", "", e(0, 4), [4], ""),
        (21, "Dani's house", "EXT", "", e(0, 1), [4], ""),
        (25, "Dani's house: the scream", "EXT", "Day", e(0, 2), [4, 10], ""),
        (18, "Dani's house", "INT", "", e(0, 1), [5], ""),
        (20, "Dani's living room", "INT", "", e(0, 3), [4, 5], ""),
        (22, "Dani's living room", "INT", "", e(0, 6), [4, 5], ""),
        (23, "Dani's bedroom", "INT", "", e(0, 3), [4], ""),
        (24, "Dani's hallway", "INT", "", e(0, 2), [4], ""),
    ]),
    ("Sun Aug 25", "Dani day", "7:00 a.m.", [
        (2, "Dani's house: the box", "EXT", "", e(0, 2), [1], ""),
        (1, "Dani's living room", "INT", "Day", e(0, 2), [1], ""),
        (3, "Dani's kitchen: opening the box", "INT", "", e(0, 7), [1, 5], ""),
        (4, "Dani's bedroom", "INT", "", e(0, 2), [1], ""),
        (5, "Dani's kitchen", "INT", "", e(0, 3), [5], ""),
        (6, "Dani's house: Dani drives off", "EXT", "", e(0, 1), [1],
         "Has to be during daylight - can't shoot first, costume change."),
        (31, "Dani's house", "INT", "", e(0, 3), [1], ""),
        (32, "Dani's hallway", "INT", "", e(0, 2), [1], ""),
        (33, "Dani's bathroom", "INT", "", e(0, 2), [1], ""),
        (34, "Dani's hallway", "INT", "", e(0, 2), [1], ""),
        (35, "Dani's bathroom", "INT", "", e(0, 2), [1], ""),
        (37, "Dani's bathroom", "INT", "", e(0, 2), [1], ""),
        (38, "Dani's hallway", "INT", "", e(0, 1), [1, 5], ""),
        (39, "Dani's bathroom", "INT", "", e(0, 5), [1, 5], ""),
        (41, "Dani's living room", "INT", "Day", e(0, 2), [5], ""),
        (42, "The hallway outside the bathroom", "INT", "", e(0, 2), [5], ""),
        (43, "The hallway outside the bathroom", "INT", "", e(0, 2), [5], ""),
        (44, "Down the hallway toward the bathroom", "INT", "", e(0, 1), [5], ""),
        (45, "The hallway outside the bathroom", "INT", "", e(0, 2), [5], ""),
        (36, "Dani's hallway", "INT", "", e(0, 1), [5], ""),
        (40, "Dani's house: the scream", "EXT", "", e(0, 1), [1], ""),
        (10, "Dani's house: Dani pulls in", "EXT", "Night", e(0, 1), [1], ""),
        (30, "Dani's house: Dani's car pulls in", "EXT", "Night", e(0, 2), [1], ""),
        (11, "Dani's kitchen: time passes", "INT", "Night", e(0, 2), [5],
         "This is a special lighting shot, MAY shoot on another day if we have time."),
    ]),
]

# ------------------------------------------------------------ the budget (EP Budgeting), as delivered
# (account, name, group, cash total, [(line, what, how it was covered)])
BUDGET = [
    (1000, "Story and rights", "ATL", 35, [("Copyright registration", "1 flat at $35", "cash")]),
    (1100, "Producers", "ATL", 0, [("Executive producer", "3 months", "pro bono"), ("Associate producer", "5 months", "pro bono")]),
    (1200, "Directors", "ATL", 0, [("Director", "6 days", "pro bono")]),
    (1300, "Cast", "ATL", 0, [("Principal players (3)", "", "pro bono"), ("Day player: the dog", "", "pro bono")]),
    (1600, "Production staff", "BTL", 900, [("Unit production manager", "5 months", "pro bono"), ("1st assistant directors (2)", "6 days", "film students"),
        ("2nd assistant director", "6 days", "film student"), ("Script supervisor", "6 days at $150", "cash"), ("Location manager", "5 months", "pro bono"),
        ("Production assistants (2)", "6 days", "film students")]),
    (1800, "Camera", "BTL", 0, [("Director of photography", "6 days", "pro bono"), ("1st assistant camera", "6 days", "film student"),
        ("2nd assistant camera", "6 days", "film student"), ("Still photographer", "6 days", "pro bono")]),
    (1900, "Wardrobe", "BTL", 245, [("Designer", "", "pro bono"), ("Girl scout costume", "1 purchase", "cash $135"), ("Fast-food uniform", "1 purchase", "cash $100"),
        ("Ratty robe", "1 purchase", "cash $10")]),
    (2000, "Make-up and hair", "BTL", 0, [("Key make-up artist", "6 days", "pro bono")]),
    (2100, "Set dressing", "BTL", 0, [("Set decorators (2)", "6 days", "pro bono")]),
    (2200, "Props", "BTL", 170, [("Propmaster", "3 months", "pro bono"), ("Animal handler", "", "pro bono"), ("The dog", "", "pro bono"),
        ("Picture vehicles (2)", "6 days", "pro bono"), ("Breakaway plates", "1 purchase", "cash $130"), ("Dog collar, name tag, dog bowl", "3 purchases", "cash $40")]),
    (2300, "Art department", "BTL", 0, [("Production assistants (2)", "6 days", "film students")]),
    (2500, "Video", "BTL", 300, [("Video editing", "2 months", "pro bono"), ("Hard drives (2)", "2 at $150", "cash")]),
    (2600, "Sound recording", "BTL", 0, [("Production mixer", "6 days", "student"), ("Boom operator", "", "film student"),
        ("Sound equipment", "6 days", "provided by Savage Light Studios")]),
    (2700, "Set lighting", "BTL", 0, [("Gaffer", "6 days", "film student"), ("Best boy", "6 days", "film student")]),
    (3100, "Locations", "BTL", 1800, [("The house", "6 days at $200", "cash $1,200"), ("Haunted TV studio", "", "pro bono"),
        ("Science lab", "", "university location"), ("Catered meals", "6 days, 20 people at $5", "cash $600"), ("Catering staff", "6 days", "pro bono")]),
    (3400, "Editing", "POST", 0, [("Editor", "2 months", "pro bono")]),
    (3800, "Titles", "POST", 0, [("Titles", "", "provided by Savage Light Studios")]),
    (4000, "Publicity", "OTHER", 1300, [("Festival entry fees", "26 entries at $50", "cash")]),
]
GRAND_TOTAL = 4750  # as printed on the top sheet; fringes $0

# ------------------------------------------------------------ risk and change log (from the thesis reflection)
# (phase, what happened, impact, response, lesson)
RISKS = [
    ("Pre-production", "Script feedback: readers and industry professionals asked for the two leads to share a scene.",
     "The film's concept changed. Set dressing, wardrobe and props bought for the original look no longer fit, and neither did the location.",
     "Made the change, returned most purchases and found a new location. Storyboards survived, because the previs hadn't encoded the palette changes.",
     "In retrospect, the right choice: it produced the most touching scene I've filmed."),
    ("Pre-production", "The actor the lead was written for had to be out of the country, about a month before the shoot.",
     "The lead role was uncast four weeks out.", "Recast the part.", ""),
    ("Pre-production", "The 3D print of the largest rock failed four times; the hand-sculpted fix cracked the resin when heat-cured.",
     "The hero prop wasn't ready.", "Repaired it twice; the paint dried minutes before leaving for set.", ""),
    ("Production", "The new location was booked solid, so there was no tech scout.",
     "On arrival it was smaller than the photos and full of reverb. Planned jib shots were impossible, the bathroom was too small, and the crash pad didn't match the hall floor.",
     "Went handheld for the jib shots.", "No location without a tech scout."),
    ("Production", "The camera fell.", "The camera broke and a couple of files were corrupted.", "A pickup day.", ""),
    ("Production", "The dog didn't like the food bought for it and wouldn't eat.", "The hardest scene of the day got harder.",
     "It was already scheduled first in the day, as the hardest scene.", "Don't write a scene with an animal unless I can hire a well-respected trainer."),
    ("Production", "The practical effects failed: the blood shooter, the shower curtain, a modesty garment that wasn't opaque.",
     "The effects didn't work as planned on the day.", "", "Hire someone for practical effects; directing, shooting and running a blood rig at once is too much."),
    ("Production", "Working with a child actor.", "The parent expected a three-page scene to take 30 minutes.", "All of the child actor's scenes were scheduled into one day.",
     "Don't write a part for a child actor; the limits are extremely restrictive."),
]
