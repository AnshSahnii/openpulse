const API = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/v1'

export type Repo = { id:number; full_name:string; owner:string; name:string; description:string|null; html_url:string|null; language:string|null; stars:number; forks:number; open_issues:number; bookmarked?:boolean }

async function request(path:string, options:RequestInit={}) {
  const token = localStorage.getItem('openpulse_token')
  const headers:Record<string,string> = {'Content-Type':'application/json', ...(options.headers as Record<string,string> || {})}
  if (token) headers.Authorization = `Bearer ${token}`
  const res = await fetch(`${API}${path}`, {...options, headers})
  const data = await res.json().catch(()=>null)
  if (!res.ok) throw new Error(data?.detail || 'Request failed')
  return data
}
export const api = {
  register:(body:any)=>request('/auth/register',{method:'POST',body:JSON.stringify(body)}),
  login:(body:any)=>request('/auth/login',{method:'POST',body:JSON.stringify(body)}),
  me:()=>request('/auth/me'),
  search:(q:string)=>request(`/repositories/search?q=${encodeURIComponent(q)}`),
  getRepo:(owner:string,repo:string)=>request(`/repositories/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}`),
  recent:()=>request('/repositories/recent'),
  bookmarks:()=>request('/bookmarks/'),
  addBookmark:(id:number)=>request(`/bookmarks/${id}`,{method:'POST'}),
  removeBookmark:(id:number)=>request(`/bookmarks/${id}`,{method:'DELETE'})
}
