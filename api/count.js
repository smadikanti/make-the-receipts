// Tiny Edge Function: increments a Redis counter on each call and returns the
// new value as JSON. Backed by Vercel Marketplace Upstash Redis.
//
// Required env vars (auto-injected by Vercel when you add the Upstash
// integration to the project):
//   KV_REST_API_URL
//   KV_REST_API_TOKEN
//
// Seed to 50:
//   curl -X POST "$KV_REST_API_URL/set/visits/50" \
//     -H "Authorization: Bearer $KV_REST_API_TOKEN"

export const config = { runtime: "edge" };

export default async function handler() {
  const url = process.env.KV_REST_API_URL;
  const token = process.env.KV_REST_API_TOKEN;

  if (!url || !token) {
    return json({ count: null, error: "kv not provisioned" }, 503);
  }

  try {
    const res = await fetch(`${url}/incr/visits`, {
      headers: { Authorization: `Bearer ${token}` },
      cache: "no-store",
    });
    if (!res.ok) {
      return json({ count: null, error: `upstream ${res.status}` }, 502);
    }
    const data = await res.json();
    return json({ count: data.result });
  } catch (e) {
    return json({ count: null, error: "fetch failed" }, 502);
  }
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json",
      "cache-control": "no-store, max-age=0",
      "access-control-allow-origin": "*",
    },
  });
}
