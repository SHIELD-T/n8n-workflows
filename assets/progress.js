// Per-browser progress for the course site. Shared by index.html and day.html.
// Stored shape: { "6": [true, false, true, true] } = Definition of Done ticks for day 6.
window.AP = {
  key: "ap-progress",
  trackKey: "ap-track",

  load: function () {
    try { return JSON.parse(localStorage.getItem(this.key) || "{}") || {}; } catch (e) { return {}; }
  },
  save: function (state) {
    try { localStorage.setItem(this.key, JSON.stringify(state)); } catch (e) {}
  },
  percent: function (state, day) {
    var ticks = state[String(day)];
    if (!ticks || !ticks.length) return 0;
    return Math.round(ticks.filter(Boolean).length / ticks.length * 100);
  },
  touched: function (state, day) {
    var ticks = state[String(day)];
    return !!(ticks && ticks.some(Boolean));
  },
  // The first unfinished day after the last day the learner worked on.
  nextDay: function (state, days) {
    var last = 0;
    days.forEach(function (d) { if (AP.touched(state, d.day)) last = d.day; });
    if (!last) return 1;
    return AP.percent(state, last) === 100 ? Math.min(last + 1, days.length) : last;
  },

  getTrack: function () {
    try { return localStorage.getItem(this.trackKey) || ""; } catch (e) { return ""; }
  },
  setTrack: function (id) {
    try { id ? localStorage.setItem(this.trackKey, id) : localStorage.removeItem(this.trackKey); } catch (e) {}
  },

  // Industry tracks from the README. `match` is how the lessons name each track.
  tracks: [
    { id: "fintech",    label: "Fintech & payments",       match: /fintech/i },
    { id: "healthtech", label: "HealthTech",               match: /health ?tech/i },
    { id: "edtech",     label: "EdTech",                   match: /ed ?tech/i },
    { id: "ecommerce",  label: "E-commerce",               match: /e-?commerce/i },
    { id: "marketing",  label: "Marketing",                match: /marketing/i },
    { id: "logistics",  label: "Logistics",                match: /logistics/i }
  ],
  trackById: function (id) {
    return this.tracks.filter(function (t) { return t.id === id; })[0] || null;
  }
};
