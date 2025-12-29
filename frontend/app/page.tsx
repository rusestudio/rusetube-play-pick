"use client";

export default function Home() {
  const handleLogin = () => {
    window.location.href = "http://127.0.0.1:8000/auth/login";
  };

  return (
    <main style={{ padding: "2rem" }}>
      <h1>YouTube Music RAG Agent</h1>
      <p>
        AI-powered music recommendations based on your YouTube listening habits.
      </p>

     <button
  onClick={handleLogin}
  className="mt-6 flex items-center gap-2 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
>
  <img
    src="https://developers.google.com/identity/images/g-logo.png"
    alt="Google"
    width={18}
    height={18}
  />
  Login with Google
</button>

    </main>
  );
}
