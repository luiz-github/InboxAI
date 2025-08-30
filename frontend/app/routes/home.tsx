import type { Route } from "./+types/home";
import { Home } from "../pages/public/home/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Home" }
  ];
}

export default function HomeRoute() {
  return <Home />;
}
