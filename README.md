# FLAMES Game

<p><strong>FLAMES </strong>is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.</p>

<p>How this game works:</p>
<ul>
<li>Take the two names.</li>
<li>Remove the common characters with their respective common occurrences.</li>
<li>Get the count of the characters that are left .</li>
<li>Take FLAMES letters as [“F”, “L”, “A”, “M”, “E”, “S”]</li>
<li>Start removing letter using the count we got.</li>
<li>The letter which last the process is the result.</li>
</ul>

<p><strong>Example :</strong>&nbsp;</p>

<pre>
Input:   
    player1 name: ali
    player2 name: alireza

Output: 
    Relationship status: Enemies</pre>

<p><strong>Explanation: </strong>In above given two names A and Y are common letters which are occurring one time(common count) in both names so we are removing these letters from both names. Now count the total letters that are left here it is 4. Now start removing letters one by one from FLAMES using the count we got and the letter which lasts the process is the result.</p>

<blockquote>
<p>FLAMES&nbsp;<br>counting is start from F, M is at 4th count so we remove M and start counting again but a this time start from E.&nbsp;<br>FLAES&nbsp;<br>L is at 4th count so we remove L and counting start from A.&nbsp;<br>FAES&nbsp;<br>F is at 4th count so we remove F and counting start from A.&nbsp;<br>AES&nbsp;<br>A is at 4th count so we remove A and counting start from E.&nbsp;<br>ES&nbsp;<br>S is at 4th count so we remove S. now we have only one letter remaining so this is the final answer.&nbsp;<br>E&nbsp;<br>So, the relationship is E is Enemies .</p>
</blockquote>
