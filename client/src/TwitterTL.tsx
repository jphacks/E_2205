import { spawn } from 'child_process';
import React from 'react';
import * as ReactDOM from 'react-dom';
import Data from './output.json';

function GetUser(author_id:string):number{
    return Data.includes.users.findIndex(e=>e.id==author_id);
}

function GetMedia(media_key:string):number{
    return Data.includes.media.findIndex(e=>e.media_key==media_key);
}

const TwitterTL = ()=>{
    return (
        <div className='TTL_wr'>
            {Data.data.map(v=>{
                let u_index = GetUser(v.author_id);
                let u_name:string;
                let u_username:string;
                let u_icon:string;
                if(u_index < 0){
                    u_name = "unknown";
                    u_username = "unknown";
                    u_icon = "https://pbs.twimg.com/profile_images/1582551294262534144/P09lQPRe_400x400.jpg";
                }
                else{
                    u_name = Data.includes.users[u_index].name;
                    u_username = Data.includes.users[u_index].username;
                    u_icon = Data.includes.users[u_index].profile_image_url;
                }
                let photo_srcs: string[] = [];
                if(v.attachments){
                    v.attachments.media_keys.forEach(
                        mk => {
                            let m_index = GetMedia(mk);
                            if(m_index < 0)return;
                            switch(Data.includes.media[m_index].type){
                                case "photo":
                                    photo_srcs.push(Data.includes.media[m_index].url || "");
                                    break;
                            }
                        }
                    );
                }
                return (
                <div key={v.id} className="p_parts" style={{background: "lightgray"}}>
                    <p className="p_parts_id" style={{fontSize:"15px", verticalAlign:"middle"}}>
                        <img
                            src={u_icon}
                            style={{
                                width: "30px",
                                borderRadius: "50%",
                                verticalAlign: "middle"
                            }}
                        />
                        <span style={{verticalAlign:"middle"}}>{u_name}</span>
                        <span style={{fontSize:"80%", color:"gray"}}>{"@"+u_username}</span>
                    </p>
                    <div className="p_parts_text" style={{margin: 0}}>
                        {
                            (()=>{
                                let rtn:(React.DetailedHTMLProps<React.HTMLAttributes<HTMLSpanElement>, HTMLSpanElement>|React.DetailedHTMLProps<React.AnchorHTMLAttributes<HTMLAnchorElement>, HTMLAnchorElement>)[] = [];
                                //let rtn:(string|React.DetailedHTMLProps<React.AnchorHTMLAttributes<HTMLAnchorElement>, HTMLAnchorElement>)[] = [];
                                let txt = v.text;
                                let txts:string[];
                                let atags:React.DetailedHTMLProps<React.AnchorHTMLAttributes<HTMLAnchorElement>, HTMLAnchorElement>[] = [];
                                let mch = txt.match(/http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- ./?%&=]*)?/g);
                                if(0 && mch){
                                    // URLを含む
                                    txts = txt.split(/http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- ./?%&=]*)?/g);
                                    mch.forEach(str=>{
                                        atags.push((
                                            <a key={str} href={str}>{str}</a>
                                        ));
                                    });
                                    for(let i=0; i<txts.length; i++){
                                        //
                                        rtn.push(<span>{txts[i]}</span>);
                                        if(i<txts.length-1)rtn.push(atags[i]);
                                    }
                                    return (
                                        <div>{0}</div>
                                    );
                                }
                                else{
                                    return (
                                        <div>{v.text}</div>
                                    );
                                }
                            })()
                        }
                        {photo_srcs.map(src=>(
                            <img key={src} src={src} style={{width:"100%"}}/>
                        ))}
                        <div style={{
                            textAlign: "right",
                            fontSize: "10px",
                            color: "gray"
                        }}>
                            {v.created_at}
                        </div>
                    </div>
                    <p className="p_parts_mtx" style={{margin:0}}>
                        ↩{v.public_metrics.reply_count}
                        ≫{v.public_metrics.quote_count}
                        🔁{v.public_metrics.retweet_count}
                        ♡{v.public_metrics.like_count}
                    </p>
                </div>
                );
            })}
            
        </div>
    );
}

export default TwitterTL;