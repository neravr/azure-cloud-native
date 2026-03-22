import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 100 },   // ramp up to 100 users
    { duration: '1m', target: 1000 },   // ramp up to 1000 users
    { duration: '30s', target: 1000 },  // stay at 1000 users
    { duration: '30s', target: 0 },     // ramp down
  ],
};

export default function () {
  const res = http.get('http://52.149.195.140/health');
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}