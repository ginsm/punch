const db = require('../model/db.js');
const utils = require('../utils/');

const Controller = {
  resolveCommand(argv) {
    // Determine the command that is being run
    const command = ['job', 'hours'].filter(cmd => cmd === argv.slice(2)[0]);
    const argument = argv.slice(3)[0];

    // If no command was ran then go to punch handler
    if (!command.length) return Controller.punchHandler();

    const commandHandlers = {
      job: Controller.jobHandler,
      // hours: view.displayHours(argument);
    }

    commandHandlers.job(argument);
  },

  /* SECTION Job creation/selection/viewing handler
  ========================================================================== */
  jobHandler(argument = '') {
      // if (!argument) return view.showCurrentJob()
      if(!db.exists(argument)) Controller.createJob(argument)
  },

  createJob(argument = '') {

  },

  /* SECTION Punch in/out handler
  ========================================================================== */
  punchHandler() {
    // Determine the current job
    const currentJob = db.open('state.json').job;
    const jobFile = `${currentJob}.json`;

    // Get the current job's JSON file
    const job = db.open('jobs/' + jobFile);

    // If no job is set then throw an error
    // if (!jobFile) view.errors.noJobSet()

    // Punch out if lastAction was in
    if (job.lastAction === 'in') return Controller.punchOut(job, jobFile);

    // Else punchIn
    return Controller.punchIn(job, jobFile);

  },

  punchIn(job, jobFile) {
    try {
      db.write({
        name: job.name,
        punchIn: (new Date()).toString(),
        lastAction: 'in',
        totalHours: job.totalHours,
      }, jobFile);
      // view.punchedIn(job.name);
      return true;
    } catch(err) {
      return false;
    }
  },

  punchOut(job, jobFile) {
    try {
      const newHours = utils.hourDifferenceDates(job.punchIn);
      const oldHours = job.totalHours;
      const newTotal = Number((job.totalHours + newHours).toFixed(2));
      db.write({
        name: job.name,
        punchIn: false,
        lastAction: 'out',
        totalHours: newTotal,
      }, jobFile);
      // view.punchedOut(job, newTotal, oldHours);
      return true;
    } catch(err) {
      return false;
    }
  },

}

Controller.resolveCommand(process.argv);