# Storyboard: Your First Day as a PA

**Type:** branching scenario, built as a site page in the Savage Light Studios style (`film/assets/sls.css`)
**Length:** about 15 minutes, one sitting
**Status:** built 2026-10-02 as `index.html` (from `index.src.html` + `maps/` via `build.py`); not yet published. **Setting:** a non-union indie feature in the US (confirmed). Open questions for Feral are at the end.

---

## 1. Why this course

A new production assistant's first day decides whether they're asked back. Nobody teaches the job
in a classroom: they're handed a walkie and a corner, and they learn by getting it wrong in front of
a crew. Mistakes cost takes, time and, at worst, someone's safety.

This course lets them get it wrong somewhere cheap first. It's a scenario rather than a lecture
because the job is judgment under time pressure: the rules are short, but knowing which one applies
while the camera is rolling is the hard part.

## 2. Learner

| | |
|---|---|
| **Who** | A set PA on their first professional shoot. Film school student, career changer, or friend-of-the-production. |
| **Knows** | Movies, some set vocabulary from film school or YouTube. |
| **Doesn't know** | Radio etiquette, the chain of command, what a lockup is, what to do when something's unsafe. |
| **Worries about** | Looking stupid, getting yelled at, not being asked back. |
| **Context** | Reads on a phone the night before their first call. Short screens, big tap targets. |

## 3. Objectives

By the end, the learner can:

1. **Read a call sheet** for their call time, location, parking and the nearest hospital.
2. **Use the radio** correctly: answer with "go for", confirm with "copy", keep it short, and know when to switch channels.
3. **Hold a lockup** politely and firmly from "rolling" to "cut", without touching anyone, standing out of frame and out of the actors' eyelines.
4. **Follow the chain of command**: take direction from the ADs, and send other requests through them.
5. **Stop and report a safety hazard** right away, even if it means holding the roll.
6. **Wrap out properly**: return gear, sign out, and confirm tomorrow's call.

## 4. Design

- **One day, six scenes.** Each scene is a decision point from a real shooting day, in order from call time to wrap.
- **Three meters: Crew trust, Schedule, Safety.** They start at 50 and each choice moves them. The meters
  show that good PA work balances all three, and that speed never beats safety.
- **Three choices per decision:** a best answer, a tempting answer that costs something, and a wrong
  answer. No choice is silly; each wrong answer is a mistake real new PAs make.
- **Consequences before explanations.** The learner sees what happens on set first (the AD's reply,
  a ruined take), then a short "On set" note explains the rule.
- **Two branches.** A poor lockup sends the learner to a recovery scene with the 2nd AD. Ignoring the safety
  hazard sends them to an incident scene. Both paths rejoin at wrap, so the day always finishes.
- **No game over.** A PA who gets it wrong on set is corrected, not fired, so the scenario does the same.
- **Debrief at the end.** It shows every decision, the best answer, and the rule behind it. That's the job aid
  they keep.
- **Safety is the floor.** If Safety ends below 40, the ending is the "talk with the 2nd AD" ending whatever
  the other meters say.

## 5. Characters

| Name | Role | Voice |
|---|---|---|
| **Dana** | 2nd AD, the learner's boss | Calm, clipped, busy. Praise is "nice". |
| **Marco** | Key PA, places the learner | Friendly, fast, explains once. |
| **Rae** | Grip | Protective of their gear. |
| **Jules** | Lead actor | Polite, distracted. |
| **A neighbour** | Lives on the block | Wants to get home. |

The learner is "you", unnamed. Radio lines appear as transcripts with the speaker's name.

## 6. Flow

```
Title ─ Briefing ─ S1 Call time ─ S2 Radio ─ S3 Lockup ─┬─ S4 Chain of command ─ S5 Safety ─┬─ S6 Wrap ─ Ending ─ Debrief
                                                        └─ S3b Recovery (poor lockup) ─────┘   │
                                                                     S5b Incident (hazard ignored) ┘
```

---

## 7. Screens

### Title
- Logo glow hero. Slate: `Day 1 · Exterior street · Take 1`.
- **Your First Day as a PA**
- Lede: "Call time is 6 a.m. Nobody's going to explain twice."
- Button: **Start the day**

### Briefing
- What the learner will practise (feature block): the six objectives in plain words.
- How it works: three meters, choices change them, you can't get fired, there's a debrief at the end.
- Meters shown at 50 / 50 / 50.

---

### Scene 1: Call time
**Slate:** `Scene 1 · Call Time · 5:40 a.m.`

The call sheet arrived last night. (Show a simplified call sheet: General crew call 6:00, PA call 5:30,
location, crew parking, nearest hospital, weather, the day's scenes.)

> You pull up at 5:40. Marco is already setting out cones. He looks at his watch.

**Decision: what went wrong?**

| Key | Choice | Trust | Sched | Safety | Consequence |
|---|---|---|---|---|---|
| A | "My call was 6:00, I'm early." | −10 | 0 | 0 | Marco: "General crew call is 6. PAs were 5:30. Read your line on the sheet." |
| **B** | **Apologise, ask what he needs, and check your own call next time.** | **+5** | **0** | **0** | Marco hands you a stack of sides. "Next time be here 15 early. Early is on time." |
| C | Say traffic was bad. | −5 | 0 | 0 | Marco: "Traffic's always bad." |

**On set:** PAs often have an earlier call than general crew call. Your call is on your line of the sheet.
Early is on time; on time is late.

**Second question (quick check, no meters):** "Where's the nearest hospital?" The learner taps the right
line on the call sheet. Feedback: "It's on every call sheet. Know it before you need it."

---

### Scene 2: The radio
**Slate:** `Scene 2 · The Radio · 6:15 a.m.`

Marco hands you a walkie and a surveillance earpiece. "Production's on channel 1. Don't talk on it unless
you have to."

> Radio: **Dana:** "Marco, Dana."

Marco's helping a truck back up and doesn't answer. Ten seconds later:

> Radio: **Dana:** "Anyone near basecamp?"

**Decision: you're at basecamp. What do you say?**

| Key | Choice | Trust | Sched | Safety | Consequence |
|---|---|---|---|---|---|
| **A** | **"Go for [your name], I'm at basecamp."** | **+10** | **+5** | 0 | Dana: "Need the sides for Jules in the makeup trailer." You: "Copy." |
| B | "Hi Dana, this is the new PA, I'm at basecamp right now, what do you need me to do?" | 0 | −5 | 0 | Dana: "…Need sides in makeup. Keep it short on 1." |
| C | Wait for Marco to answer. | −5 | −5 | 0 | Dana, again: "Anyone?" Marco finally answers and gives you a look. |

**On set:** Answer with "go for" and your name. Confirm with "copy". Keep channel 1 short: if it takes more
than a sentence, say "go to 2" and switch.

**Glossary flip cards (optional):** Copy · Go for · Go to 2 · Flying in · 10-1 · What's your 20?

---

### Scene 3: The lockup
**Slate:** `Scene 3 · The Lockup · 9:30 a.m.`

Marco puts you on the corner at the end of the block. "Nobody walks into the shot while we're rolling.
When you hear 'cut', let them through."

**Diagram: the lockup map** (top-down, in the Backwater Static map style). The block, the camera and its
frame, Jules on their mark, Jules's eyeline to the other actor just beside the lens, the pedestrian approach
to your corner, and three lettered spots where you could stand.

**Beat 1: where do you stand? (tap a spot on the map)**

> They're lighting the shot. Marco: "Find a spot where you can see anyone coming. I'll be back."

| Key | Spot | Trust | Sched | Safety | Consequence |
|---|---|---|---|---|---|
| **A** | **At the corner, outside the frame, behind the camera's side, with a clear view up the sidewalk** | **+5** | **+5** | 0 | Marco, passing: "Good spot." |
| B | Beside the camera, so you can hear the AD | −10 | −5 | 0 | Jules stops mid-line. Dana: "Whoever's by camera, you're in Jules's eyeline. Clear it, please." |
| C | Halfway down the block, closer to the pedestrians | −5 | −10 | 0 | The camera operator: "There's someone in the back of frame." You're the someone. |

The map redraws after each choice: the frame lights up in B and C to show what you were in.

**On set:** An actor's eyeline is where they look during the shot, usually at the other actor just beside the lens.
Never stand in it, and don't make eye contact with an actor during a take. Know where the frame is before you pick a spot:
if you can see the lens, it may see you. When in doubt, ask "Am I clear?"

**Beat 2: the neighbour**

> Radio: **Dana:** "Lock it up… Rolling!"
> A neighbour with grocery bags comes up to your corner. "I live right there. I just need to get through."

**Decision:**

| Key | Choice | Trust | Sched | Safety | Consequence | Next |
|---|---|---|---|---|---|---|
| **A** | **"We're rolling right now. It'll be about a minute. Thanks so much for waiting." Then echo "rolling" on the radio.** | **+10** | **+5** | 0 | You hear "cut", and you walk them through. They thank you. | S4 |
| B | Let them through; it's their street. | −15 | −15 | 0 | They walk into the back of the shot. Radio: "Cut! Who's got that corner?" | **S3b** |
| C | Put out an arm and block them. | −10 | 0 | −5 | They push past you, angry. Radio: "Cut!" You've touched a member of the public. | **S3b** |

**On set:** A lockup is a request, not an order. You can't legally stop the public, so be polite, give a time,
and thank them. Never touch anyone. Echo "rolling" and "cut" so the next PA hears it too.

#### Scene 3b: Recovery (branch)
**Slate:** `Scene 3b · Walk and Talk · 9:40 a.m.`

> Dana walks up. "What happened on your corner?"

| Key | Choice | Trust | Sched | Safety | Consequence |
|---|---|---|---|---|---|
| **A** | **"That was my corner. My mistake. Next time I'll ask them to wait and tell them how long."** | **+10** | 0 | 0 | Dana: "Good. It happens once." |
| B | "They said they lived there; I didn't think I could stop them." | 0 | 0 | 0 | Dana: "You can't stop them. You can ask nicely and tell them how long." |
| C | "Nobody told me what to do." | −10 | 0 | 0 | Dana: "Marco told you. Next time ask if you're not sure." |

**On set:** Own the mistake in one sentence and say what you'll do next time. ADs remember the answer more
than the mistake. Rejoins at Scene 4.

---

### Scene 4: Chain of command
**Slate:** `Scene 4 · Between Setups · 11:00 a.m.`

The crew is turning around for the reverse. Two requests reach you at once:

> **Rae (grip):** "Hey, can you grab that C-stand and move it over by the truck?"
> **Jules (actor):** "Could you tell the director I want to try the line differently?"

**Decision: what do you do?**

| Key | Choice | Trust | Sched | Safety | Consequence |
|---|---|---|---|---|---|
| **A** | **Tell Rae you'll ask Dana if you're free to help. Tell Jules you'll pass it to the 2nd AD, then radio Dana.** | **+10** | 0 | **+5** | Dana: "Copy, I'll tell the 1st. Rae can have you for five." |
| B | Move the C-stand, then walk over to the director. | −10 | −5 | −5 | Rae: "Not like that. Don't touch my gear without asking." The 1st AD intercepts you before you reach the director. |
| C | Say you're busy to both. | −5 | 0 | 0 | Jules has to find someone else; Rae carries it alone. |

**On set:** You work for the AD department. Other departments' gear belongs to them: don't touch it unless
they show you how. Messages to the director go through the ADs.

---

### Scene 5: Safety
**Slate:** `Scene 5 · The Picture Car · 2:15 p.m.`

After lunch, the scene is a car pulling up fast to the curb. The precision driver is rehearsing. You're
holding background extras on the sidewalk.

> One extra steps off the curb to take a selfie, in the car's path. The car is backing up to its first mark.
> Nobody near camera can see the extra.

**Decision:**

| Key | Choice | Trust | Sched | Safety | Consequence | Next |
|---|---|---|---|---|---|---|
| **A** | **Call "Hold the roll, person in the car's path" on channel 1, and move the extra back.** | **+10** | −5 | **+20** | Dana: "Holding! Thank you." The rehearsal resets. The stunt coordinator moves the extras' mark back. | S6 |
| B | Walk over and quietly ask the extra to step back. | 0 | 0 | −10 | The car stops a few feet away. The driver is shaken, and the stunt coordinator wants to know why nobody called it. | **S5b** |
| C | It's a rehearsal; the driver can see. Say nothing. | −10 | 0 | −25 | The driver can't see behind the car. | **S5b** |

**On set:** Anyone on set can call a hold for safety, and nobody will be angry that you did. Call it first,
then fix it. A lost minute is cheap; an injury shuts down the shoot.

#### Scene 5b: Incident (branch)
**Slate:** `Scene 5b · Safety Meeting · 2:30 p.m.`

> Nobody was hurt. The 1st AD stops work and calls the crew together. "Who had eyes on the sidewalk?"

| Key | Choice | Trust | Sched | Safety | Consequence |
|---|---|---|---|---|---|
| **A** | **"I did. I saw them step off and I should have called a hold."** | **+10** | 0 | **+10** | 1st AD: "Thank you. Next time, call it. Everyone hear that? Anyone can call it." |
| B | Say nothing. | −15 | 0 | −5 | The extra points at you. |

**On set:** After a near miss, tell the truth fast. The safety meeting exists to stop it happening twice.
Rejoins at Scene 6.

---

### Scene 6: Wrap
**Slate:** `Scene 6 · Martini Shot · 6:45 p.m.`

> Radio: **Dana:** "That's a wrap on the day. Thanks, everyone."

**Decision: what do you do before you leave?** (choose all that apply; scored as one decision)

- **Return your walkie and earpiece to Marco** ✔
- **Help pick up cones and signs from your corner** ✔
- **Check you have tomorrow's call sheet** ✔
- **Sign out with the key PA** ✔
- Head home; you've been up since 4 ✘

| Result | Trust | Sched |
|---|---|---|
| All four right, none wrong | +10 | +5 |
| Missed one or more | −5 | 0 |

**On set:** You're not wrapped until the PAs are wrapped. A missing walkie gets charged to the production.

---

### Endings (based on the meters)

| Ending | Rule | Text |
|---|---|---|
| **Asked back** | Safety ≥ 60 and Trust ≥ 60 | Dana: "Same call tomorrow. Nice work today." |
| **Day player** | Safety ≥ 40, not "Asked back" | Marco: "Dana says they've got you down as a maybe for next week." |
| **Talk with the 2nd AD** | Safety < 40 | Dana: "Can I have a minute? Let's go through today." Leads into the debrief. |

Final meters show with a one-line read of each ("Crew trust: the crew would work with you again").

### Debrief
- A table of every decision: what you chose, the best answer, and the rule.
- **The PA's first-day card** (on screen and as a one-page printable PDF, `pa-first-day-card.pdf`): radio words, the lockup script, the chain of command,
  "call it first", and the wrap checklist.
- Button: **Run the day again**

---

## 8. Diagrams

Top-down set maps in the style of the Backwater Static battlemaps, recoloured to the Savage Light Studios palette:
thin outlined walls and kerbs, simple furniture and vehicle shapes, dashed zones, a scale bar, labels in caps,
and a legend underneath.

| Map | Scene | Shows |
|---|---|---|
| **Basecamp** | 1–2 | Trucks, makeup trailer, crew parking, sign-in, the walk to set. Where "basecamp" is when Dana calls. |
| **The lockup** | 3 | Camera, frame cone, actors' marks, eyeline, the pedestrian route, lockup spots A/B/C. Interactive in Beat 1. |
| **The picture car** | 5 | The car's path and marks, the driver's blind spot behind the car, the extras' holding area, the hazard. |
| **The PA's first-day card** | Debrief | A small version of the lockup map with the do's: out of frame, out of eyeline, view of the approach. |

Map key (same on every map):
- **Tan** lines: buildings, kerbs, furniture
- **Cyan** dashed cone: the camera's frame
- **Glow** dotted line: an eyeline
- **Ember** dashed zone: a hazard or no-go area, always labelled
- **White** circles with letters: places the learner can choose
- **Scale bar** in metres and feet

Built as inline SVG, so they're sharp on a phone, readable by screen readers through a title and description, and
recolourable from `sls.css`.

## 9. Build notes

- One HTML page, `film/pa-first-day/index.html`, with `sls.css` and a small scenario script.
  Scenes are data (JSON in the page), so wording changes don't touch code.
- Meter values are kept in the page, not saved; refresh starts a new day.
- Works without JavaScript as a readable script with the best answers marked, the same rule as the
  20 Below site courses.
- Phone first. Choices are full-width buttons. Each meter shows its number as well as its bar.
- Accessibility: meter changes are announced (aria-live), choices are real buttons, and consequences are
  labelled, never shown by colour alone.

## 10. Evaluation (feeds sample 3)

- **Level 1:** a two-question reaction check after the debrief ("How ready do you feel for your first day?").
- **Level 2:** the debrief score: best answers out of the scored decisions.
- **Levels 3 and 4:** described in the evaluation plan (sample 3): what a 2nd AD would observe on day one, and
  how often new PAs are asked back.

---

## Open questions for Feral (ask one at a time)

1. ~~What kind of shoot?~~ Non-union indie feature, US (Feral, 2026-10-02).
2. ~~Radio conventions?~~ Confirmed as drafted: channel 1 / "go to 2", "go for", "copy", "flying in", "10-1", "What's your 20?" (Feral, 2026-10-02).
3. ~~Anything missing?~~ Add eyelines to the lockup scene, and add set diagrams like the Backwater Static maps (Feral, 2026-10-02).
4. ~~Printable card?~~ Yes: the PA's first-day card is on the debrief screen and as a printable PDF (Feral, 2026-10-02). Map style approved the same day.
