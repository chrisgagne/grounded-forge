import { loadConfig } from '../config.js';
import { openDatabase } from './index.js';
import { migrateDown, migrateUp } from './migrate.js';

const [command = 'up', stepsArg = '1'] = process.argv.slice(2);
const db = openDatabase(loadConfig().databasePath);

if (command === 'up') {
  const applied = migrateUp(db);
  console.log(applied.length ? `applied: ${applied.join(', ')}` : 'already up to date');
} else if (command === 'down') {
  const reverted = migrateDown(db, { steps: Number(stepsArg) });
  console.log(reverted.length ? `reverted: ${reverted.join(', ')}` : 'nothing to revert');
} else {
  console.error('usage: npm run migrate -- up | down [steps]');
  process.exitCode = 2;
}
