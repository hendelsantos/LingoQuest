import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  cacheComponents: true,
  partialPrefetching: true,
  // Django/DRF contracts use trailing slashes. Preserve them through the proxy.
  skipTrailingSlashRedirect: true,
  async rewrites() {
    const apiBaseUrl =
      process.env.NEXT_INTERNAL_API_BASE_URL ?? "http://127.0.0.1:8000";

    return [
      {
        source: "/api/:path*/",
        destination: `${apiBaseUrl}/api/:path*/`,
      },
      {
        source: "/api/:path*",
        destination: `${apiBaseUrl}/api/:path*`,
      },
      {
        source: "/health/",
        destination: `${apiBaseUrl}/health/`,
      },
    ];
  },
  turbopack: {
    rules: {
      "*.css": {
        loaders: ["@tailwindcss/turbopack"],
        as: "*.css",
      },
    },
  },
};

export default nextConfig;
